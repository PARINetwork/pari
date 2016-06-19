from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .views import add_author
from .models import Author


@hooks.register('register_admin_urls')
def author_admin_urls():
    return [
        url(r'^authors/add/$', add_author, name='author_add'),
    ]


class AuthorAdmin(ModelAdmin):
    model = Author
    menu_label = _("Authors")
    menu_icon = "user"
    search_fields = ('name', 'email', )

modeladmin_register(AuthorAdmin)
