from django.conf.urls import patterns, url

from wagtail.wagtailcore import hooks

from .views import add_audio


@hooks.register('register_admin_urls')
def location_admin_urls():
    return [
        url(r'^audio/add/$', add_audio, name='audio_add'),
    ]
