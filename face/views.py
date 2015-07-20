from django.views.generic import ListView
from django.db import connections

from .models import Face


class FaceList(ListView):
    context_object_name = "faces"

    def get_queryset(self):
        qs = Face.objects.raw('SELECT DISTINCT ON (substr(district, 1, 1)) * '
                              'FROM face_face JOIN location_location ON '
                              'face_face.location_id=location_location.id '
                              'JOIN wagtailcore_page ON wagtailcore_page.id=face_face.page_ptr_id '
                              'ORDER BY substr(district, 1, 1)')
        return qs


class FaceDetail(ListView):
    context_object_name = "faces"
    model = Face
    template_name = "face/face.html"

    def get_queryset(self):
        alphabet = self.kwargs['alphabet']
        return Face.objects.filter(location__district__istartswith=alphabet)
