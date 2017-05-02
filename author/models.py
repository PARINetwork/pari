from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    email = models.EmailField(null=True, blank=True)
    twitter_username = models.CharField(max_length=50, null=True, blank=True)
    facebook_username = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ForeignKey('core.AffixImage', null=True, blank=True)


    def __init__(self, *args, **kwargs):
        self.__class__.panels = [
            FieldPanel('name'),
            FieldPanel('email'),
            FieldPanel('twitter_username'),
            FieldPanel('facebook_username'),
            FieldPanel('website'),
            MultiFieldPanel([
                FieldPanel('bio_%s' % ii[0]) for ii in settings.LANGUAGES
            ], heading="Bio", classname="collapsible"),
        ]
        super(Author, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Author, self).save(**kwargs)

    def get_absolute_url(self):
        name = "author-detail"
        return reverse(name, kwargs={"slug": self.slug})