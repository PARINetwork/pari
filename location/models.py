from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    point = models.PointField(srid=4326)

    # Below points are to prevent reverse caching
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=100, null=True, blank=True)
    panchayat = models.CharField(max_length=100, null=True, blank=True)

    sub_district_type = models.ForeignKey("SubDistrictType",
                                             related_name="location", null=True, blank=True)

    sub_district_name = models.CharField(max_length=100, null=True, blank=True)

    objects = models.GeoManager()

    def __str__(self):
        location = filter(lambda x: x, [self.name, self.panchayat, self.region, self.sub_district_name, self.district, self.state])
        return ", ".join(location)

    @property
    def address(self):
        addr = self.name
        addr += ", " + self.sub_district_name if self.sub_district_name else ""
        addr += ", " + self.district if self.district else ""
        addr += ", " + self.state if self.state else ""
        return addr

    class Meta:
        unique_together = ["name", "district", "state", "panchayat", "sub_district_name"]
        ordering = ["name"]

@python_2_unicode_compatible
class SubDistrictType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
