from django.conf.urls import url

from wagtail.core import hooks

from .views import add_audio


@hooks.register('register_admin_urls')
def location_admin_urls():
    return [
        url(r'^audio/add/$', add_audio, name='audio_add'),
    ]
