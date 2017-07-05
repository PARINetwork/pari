from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter
def get_type(obj):
    type_ = obj.__class__.__name__.lower()

    if type_ == 'album':
        return 'talking_album' if obj.slides.first().audio else 'photo_album'
    if type_ == 'article':
        categories = obj.categories.values_list('name', flat=True)
        if 'VideoZone' in categories:
            return 'video_zone'
        if 'AudioZone' in categories:
            return 'audio_zone'
    return type_

@register.filter
def show_separator(obj):
    type_ = obj.__class__.__name__.lower()
    if type_ == 'article':
        if not obj.show_year:
            return False
    return True


@register.filter
def get_locations(obj):
    type_ = obj.__class__.__name__.lower()
    if type_ == 'article':
        return obj.locations.all()
    if type_ == 'album' or type_ == 'face':
        return obj.locations
    return []

@register.filter
def get_photographers(obj):
    type_ = obj.__class__.__name__.lower()
    if type_ == 'article':
        return obj.authors.all()
    if type_ == 'album' or type_ == 'face':
        return obj.photographers
    return []

@register.filter
def get_strap(obj):
    type_ = obj.__class__.__name__.lower()
    if type_ == 'article':
        return obj.strap
    if type_ == 'album':
        return BeautifulSoup(obj.description).get_text()
    return ''