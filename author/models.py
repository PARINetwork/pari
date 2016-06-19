from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    email = models.EmailField(null=True, blank=True)
    twitter_username = models.CharField(max_length=50, null=True, blank=True)
    facebook_username = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ForeignKey('core.AffixImage', null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('twitter_username'),
        FieldPanel('facebook_username'),
        FieldPanel('website'),
        MultiFieldPanel([
            FieldPanel('bio'),
        ], heading="Bio", classname="collapsible"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
