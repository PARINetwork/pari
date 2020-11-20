from __future__ import unicode_literals

from django.db import models
import django.db.models.deletion
from django.conf import settings
from django.utils.text import slugify
from six import python_2_unicode_compatible
from django.urls import reverse

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    email = models.EmailField(null=True, blank=True)
    twitter_username = models.CharField(max_length=50, null=True, blank=True)
    facebook_username = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ForeignKey('core.AffixImage', null=True, blank=True, on_delete=django.db.models.deletion.PROTECT)


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

    @property
    def twitter_handle(self):
        if self.twitter_username:
            return self.twitter_username.replace('@', '')
        return ""

    def save(self, **kwargs):
        if not self.slug:
            copySlug = self.slug = slugify(self.name)[:50]
            import itertools
            for x in itertools.count(1):
                if not Author.objects.filter(slug=self.slug).exists():
                    break

                self.slug = "%s%d" % (copySlug[:50 - len(str(x))], x)

        return super(Author, self).save(**kwargs)

    def get_absolute_url(self):
        name = "author-detail"
        return reverse(name, kwargs={"slug": self.slug})
