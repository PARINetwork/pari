from django.db.models import Q
from django.views.generic import ListView
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
        context["title"] = 'FACES'
        context["sub_heading"] = 'People from every indian district'
        context["tab"] = 'gallery'
        context["current_page"] = 'face-list'
        return context


class FaceDetail(ListView):
    context_object_name = "faces"
    model = Face
    template_name = "face/face.html"

    def get_queryset(self):
        # TODO: Should return queryset instead of list
        # TODO: Improve query performance
        alphabet = self.kwargs['alphabet']
        faces = Face.objects.live().filter(
            Q(location__district__istartswith=alphabet) | Q(image__locations__district__istartswith=alphabet)
        ).select_related('location', 'location__sub_district_type') \
            .prefetch_related('image__photographers', 'image__locations').distinct()
        faces_with_matching_district_added = [self.with_matching_district(face, alphabet) for face in faces]
        faces_ordered_by_matching_district = sorted(faces_with_matching_district_added,
                                                    key=lambda f: f.matching_district)
        return faces_ordered_by_matching_district

    def get_context_data(self):
        context = super(FaceDetail, self).get_context_data()
        context["alphabet"] = self.kwargs["alphabet"]
        context["share_sub_heading"] = 'People from every Indian district'
        context['site'] = RequestSite(self.request)
        context["slug"] = self.kwargs.get("slug")
        if context["slug"]:
            try:
                context["face"] = next(face for face in self.get_queryset() if face.slug == context["slug"])
            except StopIteration:
                pass
        context["current_page"] = 'face-district'
        return context

    @staticmethod
    def with_matching_district(face, alphabet):
        if face.location.district.lower().startswith(alphabet.lower()):
            face.matching_district = face.location.district
            return face

        face_image_location = face.image.locations.filter(district__istartswith=alphabet).first()
        face.matching_district = face_image_location and face_image_location.district or ''
        return face
