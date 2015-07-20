from django.conf.urls import patterns, url

from wagtail.wagtailcore import hooks

from .views import add_author


@hooks.register('register_admin_urls')
def author_admin_urls():
    return [
        url(r'^authors/add/$', add_author, name='author_add'),
    ]
