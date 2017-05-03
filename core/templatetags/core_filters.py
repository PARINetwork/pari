from django import template

register = template.Library()


@register.filter
def get_type(obj):
    type_ = obj.__class__.__name__.lower()

    if type_ == 'album':
        return 'talking_album' if obj.slides.first().audio else 'photo_album'
    return type_
