import requests

from django.views.generic import DetailView, ListView
from django.urls import reverse
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse, Http404
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.modal_workflow import render_modal_workflow

from album.models import Album, AlbumSlide

from core.utils import get_slide_detail


class AlbumList(ListView):
    model = Album

    def get_queryset(self):
        qs = super(AlbumList, self).get_queryset()
        qs = qs.filter(live=True)
        return qs

    def set_album_data(self, context, album_qs, title, subtitle, *args, **kwargs):
        if title == 'Talking Albums':
            slide_id = AlbumSlide.objects.exclude(audio='').values_list('page__id')
        else:
            slide_id = AlbumSlide.objects.filter(audio='').values_list('page__id')
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


class TaggedAlbumList(AlbumList):
    def get_queryset(self):
        qs = super(TaggedAlbumList, self).get_queryset()
        qs = qs.filter(tags__name__iexact=self.kwargs['tag'])
        return qs


class AlbumDetail(DetailView):
    context_object_name = "album"
    model = Album

    def get_object(self, queryset=None):
        obj = super(AlbumDetail, self).get_object(queryset)
        if self.request.GET.get("preview"):
            obj = obj.get_latest_revision_as_page()
            return obj
        if not obj.live:
            raise Http404
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumDetail, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        album = Album.objects.get(slug=slug)
        json_response = get_slide_detail(album)
        if album.slides.last().audio != '':
            context['album_type'] = 'talking_album'
        else:
            context['album_type'] = 'photo_album'
        if json_response:
            context['json_response'] = json_response.content.decode("utf-8")
        return context

    def get_template_names(self):
        names = super(AlbumDetail, self).get_template_names()
        if self.request.path == reverse("image-collection-image-list",
                                        kwargs={"slug": self.kwargs["slug"]}):
            names.insert(0, "album/albumslide_list.html")
        return names

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
