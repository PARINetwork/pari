from django import forms
from django.contrib.gis.forms import PointField, OSMWidget
from django.conf import settings

from .models import Location


class LeafletMapWidget(OSMWidget):
    template_name = "gis/admin/leaflet.html"
    default_lat = settings.MAP_CENTER[0]
    default_lon = settings.MAP_CENTER[1]
    default_zoom = 4
    map_srid = 4326

    def __init__(self, attrs=None):
        super(LeafletMapWidget, self).__init__(attrs=attrs)
        self.attrs['default_zoom'] = self.default_zoom


class LocationAdminForm(forms.ModelForm):
    state = forms.CharField(max_length=50,
                            widget=forms.Select(choices=settings.STATE_CHOICES))
    point = PointField(widget=LeafletMapWidget())

    class Meta:
        model = Location
        fields = ["point", "name", "block", "district", "region", "state"]
