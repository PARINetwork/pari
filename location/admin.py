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
    search_fields = ["name", "district", "panchayat", "region", "state", "sub_district_value"]
    list_filter = ["state"]
    list_display = ["name", "district", "panchayat", "region", "state", "sub_district_value"]

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.name[:50])
        obj.save()

admin.site.register(Location, LocationAdmin)
