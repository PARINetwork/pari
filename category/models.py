from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from modelcluster.fields import ParentalKey


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey('core.AffixImage',
                              null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name="category_for_image")
    order = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["order"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("story-detail", kwargs={"slug": self.slug})
