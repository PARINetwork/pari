import requests

from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.cache import cache

from wagtail.wagtailadmin.modal_workflow import render_modal_workflow

from album.models import Album, AlbumSlide
from django.template.defaulttags import register


class AlbumList(ListView):
    model = Album

    def get_queryset(self):
        qs = super(AlbumList, self).get_queryset()
        qs = qs.filter(live=True)
        return qs

    def get_context_data(self, *args, **kwargs):

        context = super(AlbumList, self).get_context_data(*args, **kwargs)

        filter_param = self.kwargs['filter']
        if filter_param == "talking":
            slide_id = AlbumSlide.objects.exclude(audio='').values_list('page__id')
            qs = self.get_queryset().filter(id__in=slide_id)
            context['albums'] = qs
            context['tab'] = 'gallery'
            context["title"] = "Talking Albums"
            context["sub_heading"] = 'pictures, through the author\'s eyes'
        elif filter_param == "other":
            slide_id = AlbumSlide.objects.filter(audio='').values_list('page__id')
            qs = self.get_queryset().filter(id__in=slide_id)
            context['albums'] = qs
            context['tab'] = 'gallery'
            context["title"] = "Albums"
            context["sub_heading"] = 'pictures, through the author\'s eyes'
        else:
            context['albums'] = self.get_queryset()
        photographers = {}
        for album in context["albums"]:
            slide_photo_graphers= []
            for slide in album.slides.all():
                slide_photo_graphers.extend(slide.image.photographers.all())
            photographers[album.id] = set(slide_photo_graphers)
        context["photographers"] = photographers
        return context


class AlbumDetail(DetailView):
    context_object_name = "album"
    model = Album

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
        request, "album/add_audio.html", None,  {
            "add_object_url": reverse("audio_add"),
            "name": "Audio",
            "obj_id": obj_id,
            "access_token": access_token,
            "client_id": sc["CLIENT_ID"]
        })
