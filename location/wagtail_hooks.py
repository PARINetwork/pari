from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.views import CreateView, EditView

from .models import Location
from .forms import LocationAdminForm
from .views import add_location


@hooks.register('register_admin_urls')
def location_admin_urls():
    return [
        url(r'^locations/add/$', add_location, name='locations_add'),
        # Below for FK fields like in Faces
        url(r'^location/add/$', add_location, name='locations_add'),
    ]


class LocationCreateView(CreateView):
    def get_form_class(self):
        return LocationAdminForm


class LocationEditView(EditView):
    def get_form_class(self):
        return LocationAdminForm


class LocationAdmin(ModelAdmin):
    model = Location
    create_view_class = LocationCreateView
    edit_view_class = LocationEditView
    menu_label = _("Locations")
    menu_icon = "home"
    list_display = ('name', 'district', 'state')
    search_fields = ('name', 'district', 'state')

# modeladmin_register(LocationAdmin)
