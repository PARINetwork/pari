from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from django.contrib.gis.geos import Point
from django.contrib.gis.gdal import CoordTransform, SpatialReference
from django.contrib.gis.forms import PointField
from django.utils.text import slugify

from .models import Location
from .forms import LocationAdminForm

class LocationAdmin(GeoModelAdmin):
    max_extent = False
    max_resolution = False
    form = LocationAdminForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name)
        obj.save()

admin.site.register(Location, LocationAdmin)
