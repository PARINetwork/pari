from django.views.generic import ListView
from django.db import connections
from django.contrib.sites.requests import RequestSite

from .models import Face


class FaceList(ListView):
    context_object_name = "faces"

    def get_queryset(self):
        qs = Face.objects.live().raw(
            'SELECT DISTINCT ON (substr(district, 1, 1)) * '
            'FROM face_face JOIN location_location ON '
            'face_face.location_id=location_location.id '
            'JOIN wagtailcore_page ON wagtailcore_page.id=face_face.page_ptr_id '
            'ORDER BY substr(district, 1, 1), first_published_at DESC')
        return qs

    def get_context_data(self):
        context = super(FaceList, self).get_context_data()
        context["title"] = 'Faces'
        context["sub_heading"] = 'FACIAL DIVERSITY FROM EVERY INDIAN DISTRICT'
        context["tab"] = 'gallery'
        context["current_page"] = 'face-list'
        return context

class FaceDetail(ListView):
    context_object_name = "faces"
    model = Face
    template_name = "face/face.html"

    def get_queryset(self):
        alphabet = self.kwargs['alphabet']
        return Face.objects.live().filter(
            location__district__istartswith=alphabet
        ).order_by('-first_published_at')

    def get_context_data(self):
        context = super(FaceDetail, self).get_context_data()
        context["alphabet"] = self.kwargs["alphabet"]
        context['site'] = RequestSite(self.request)
        context["slug"] = self.kwargs.get("slug")
        if context["slug"]:
            try:
                context["face"] = self.get_queryset().get(slug=context["slug"])
            except Face.DoesNotExist:
                pass
        context["current_page"] = 'face-district'
        return context
