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

    sub_district_type = models.ForeignKey("SubDistrictType",
                                             related_name="location", null=True, blank=True)

    sub_district_type_value = models.CharField(max_length=100, null=True, blank=True)

    objects = models.GeoManager()

    def __str__(self):
        return "{0}, {1}, {2}".format(self.name, self.district,
                                                 self.state)

    @property
    def address(self):
        addr = self.name
        addr += ", " + self.sub_district_type_value if self.sub_district_type_value else ""
        addr += ", " + self.district if self.district else ""
        addr += ", " + self.state if self.state else ""
        return addr

    class Meta:
        unique_together = ["name", "district", "state"]
        ordering = ["name"]

@python_2_unicode_compatible
class SubDistrictType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
