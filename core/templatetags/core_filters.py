from django import template

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
