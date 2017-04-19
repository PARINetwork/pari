from django import template

register = template.Library()


@register.filter(name='alt_text')
def alt_text(face):
    return '{name} is a {occupation} from {location}'.format(name=face.title, occupation=face.occupation or 'person',
                                                             location=face.location or 'India')


@register.filter
def matching_district(face, starts_with):
    if face.location.district.lower().startswith(starts_with.lower()):
        return face.location.district

    face_image_location = face.image.locations.filter(district__istartswith=starts_with).first()
    return face_image_location and face_image_location.district or ''
