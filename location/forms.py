from django import forms
from django.contrib.gis.forms import PointField, OSMWidget
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

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

    def clean_sub_district_name(self):
        sub_district_name = self.cleaned_data["sub_district_name"]
        sub_district_type = self.cleaned_data["sub_district_type"]
        if not sub_district_type and sub_district_name:
            raise forms.ValidationError(_("Sub district type has to be chosen first"))
        return sub_district_name

    class Meta:
        model = Location
        fields = ["point", "name", "district", "region", "state", "panchayat", "sub_district_type", "sub_district_name"]
