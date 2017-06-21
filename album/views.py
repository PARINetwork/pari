import requests
import datetime

from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.rich_text import RichText
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.modal_workflow import render_modal_workflow

from album.models import Album, AlbumSlide
from author.models import Author
from django.template.defaulttags import register


class AlbumList(ListView):
    model = Album

    def get_queryset(self):
        qs = super(AlbumList, self).get_queryset()
        qs = qs.filter(live=True)
        return qs

    def set_album_data(self, context, album_qs, title, subtitle, *args, **kwargs):
        slide_id = AlbumSlide.objects.exclude(audio='').values_list('page__id')
        qs = album_qs.filter(id__in=slide_id)
        qs = qs.order_by('-first_published_at')
        context['albums'] = qs
        context['tab'] = _("gallery")
        context["title"] = title
        context["sub_heading"] = subtitle

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumList, self).get_context_data(*args, **kwargs)
        album_qs = self.get_queryset().prefetch_related('slides')
        filter_param = self.kwargs['filter']
        if filter_param == "talking":
            self.set_album_data(context, album_qs, _("Talking Albums"), _("Pictures and their spoken story"))
        elif filter_param == "other":
            self.set_album_data(context, album_qs, _("Photo Albums"), _("Through many different lenses"))
        else:
            context['albums'] = album_qs
        photographers = {}
        for album in context["albums"]:
            slide_photo_graphers = []
            for slide in album.slides.all():
                slide_photo_graphers.extend(slide.image.photographers.all())
            photographers[album.id] = set(slide_photo_graphers)
        context["photographers"] = photographers
        context["current_page"] = 'album-list'
        return context


class AlbumDetail(DetailView):
    context_object_name = "album"
    model = Album

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumDetail, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        album = Album.objects.get(slug=slug)
        if album.slides.last().audio != '':
            context['album_type'] = 'talking_album'
        else:
            context['album_type'] = 'photo_album'
        return context

    def get_template_names(self):
        names = super(AlbumDetail, self).get_template_names()
        if self.request.path == reverse("image-collection-image-list",
                                        kwargs={"slug": self.kwargs["slug"]}):
            names.insert(0, "album/albumslide_list.html")
        return names


def get_slide_detail(request, slug):
    album = Album.objects.get(slug=slug)
    response_data = {}
    response_data['slides'] = []
    photographers = []
    slide_photo_graphers = []
    for slide in album.slides.all():
        slide_photo_graphers.extend(map(lambda photographer_name: photographer_name.name.encode('UTF-8'),
                                               slide.image.photographers.all()))
    photographers_of_album = list(set(slide_photo_graphers))
    for index,slide in enumerate(album.slides.all(),start=0):
        slide_dict = dict([('type', 'image'), ('show_title', "True"), ('album_title', album.title)])
        slide_dict['src'] = slide.image.file.url
        slide_dict['src_resized'] = slide.image.get_rendition('height-876').url
        block = blocks.RichTextBlock()
        description_value = RichText(slide.description)
        slide_dict['description'] = block.render(description_value)
        slide_dict['album_description'] = album.description
        slide_dict['url'] = request.build_absolute_uri().replace(".json", "")
        slide_dict['slide_photographer'] = map(lambda photographer_name: photographer_name.name.encode('UTF-8'),
                                               slide.image.photographers.all())
        if index == 0:
            slide_dict['slide_photographer'] =photographers_of_album
            print index
        photographers.extend(set(slide.image.photographers.all()))
        d = datetime.datetime.strptime(str(album.first_published_at)[:10], "%Y-%m-%d")
        date = d.strftime('%d %b,%Y')
        slide_dict['image_captured_date'] = date
        image_location = slide.image.locations.first()
        slide_dict['slide_location'] = "%s, %s" % (image_location.district, image_location.state) if image_location else ''
        slide_dict['track_id'] = slide.audio
        response_data['slides'].append(slide_dict)

    response_data['authors'] = []
    for photographer in set(photographers):
        photographer_dict = dict(
            [('type', 'inline'), ('show_title', "False"), ('name', photographer.name), ('bio', photographer.bio_en),
             ('twitter_username', photographer.twitter_handle), ('facebook_username', photographer.facebook_username),
             ('email', photographer.email), ('website', photographer.website), ('author_url', reverse('author-detail', kwargs={'slug': photographer.slug}))])
        response_data['authors'].append(photographer_dict)
    return JsonResponse(response_data)


def add_audio(request):
    sc = settings.SOUNDCLOUD_SETTINGS
    access_token = None
    if not cache.get("sc_access_token"):
        response = requests.post(sc["API_URL"] + "/oauth2/token/",
                                 data={
                                     "client_id": sc["CLIENT_ID"],
                                     "client_secret": sc["CLIENT_SECRET"],
                                     "username": sc["USERNAME"],
                                     "password": sc["PASSWORD"],
                                     "grant_type": "password"
                                 }
                                 )
        if response.ok:
            access_token = response.json()["access_token"]
            cache.set("sc_access_token",
                      access_token,
                      response.json()["expires_in"])
    else:
        access_token = cache.get("sc_access_token")
    obj_id = request.GET.get("id")
    return render_modal_workflow(
        request, "album/add_audio.html", None, {
            "add_object_url": reverse("audio_add"),
            "name": "Audio",
            "obj_id": obj_id,
            "access_token": access_token,
            "client_id": sc["CLIENT_ID"]
        })
