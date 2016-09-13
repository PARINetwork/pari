from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    point = models.PointField(srid=4326)

    # Below points are to prevent reverse caching
    block = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=100, null=True, blank=True)

    objects = models.GeoManager()

    def __str__(self):
        return "{0}, {1}, {2} ({3}, {4})".format(self.name, self.district,
                                                 self.state,
                                                 self.point.x, self.point.y)

    @property
    def address(self):
        addr = self.name
        addr += ", " + self.block if self.block else ""
        addr += ", " + self.district if self.district else ""
        addr += ", " + self.state if self.state else ""
        return addr

    class Meta:
        unique_together = ["name", "district", "state"]
        ordering = ["name"]
