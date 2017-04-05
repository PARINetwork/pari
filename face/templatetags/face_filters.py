from django import template

register = template.Library()
@register.filter(name='alt_text')
def alt_text(face):
    return '{name} is a {occupation} from {location}'.format(name=face.title, occupation=face.occupation or 'person', location=face.location or 'India')