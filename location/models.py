from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
import django.db.models.deletion


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
                                          related_name="location", null=True, blank=True, on_delete=django.db.models.deletion.PROTECT)

    sub_district_name = models.CharField(max_length=100, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        location = filter(lambda x: x,
                          [self.name, self.panchayat, self.region, self.sub_district_name, self.district, self.state])
        return ", ".join(location)

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)
        computed_slug = slugify("%s-%s" % (self.id, self.name))[:50]
        if computed_slug != self.slug:
            self.slug = computed_slug
            Location.objects.filter(pk=self.id).update(slug=computed_slug)

    @property
    def address(self):
        addr = self.name
        addr += ", " + self.sub_district_name if self.sub_district_name else ""
        addr += ", " + self.district if self.district else ""
        addr += ", " + self.state if self.state else ""
        return addr

    @property
    def minimal_address(self):
        addr = self.district
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
