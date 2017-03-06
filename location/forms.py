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
    sub_district_type_value = forms.CharField(
        label=_("Sub district type value"),
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False)

    def clean_sub_district_type_value(self):
        sub_district_type_value = self.cleaned_data["sub_district_type_value"]
        sub_district_type = self.cleaned_data["sub_district_type"]
        if not sub_district_type and sub_district_type_value:
            raise forms.ValidationError(_("Sub district type has to be chosen first"))
        return sub_district_type_value

    class Meta:
        model = Location
        fields = ["point", "name", "district", "region", "state", "sub_district_type", "sub_district_type_value"]
