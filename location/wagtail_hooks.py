from django.conf.urls import patterns, url

from wagtail.wagtailcore import hooks

from .views import add_location


@hooks.register('register_admin_urls')
def location_admin_urls():
    return [
        url(r'^locations/add/$', add_location, name='locations_add'),
        # Below for FK fields like in Faces
        url(r'^location/add/$', add_location, name='locations_add'),
    ]
