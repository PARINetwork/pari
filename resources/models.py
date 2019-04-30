from __future__ import unicode_literals

import json
import urllib2

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalManyToManyField, ParentalKey

from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from core.utils import SearchBoost


class ResourceTag(TaggedItemBase):
    content_object = ParentalKey('resources.Resource', related_name='tagged_items')


@python_2_unicode_compatible
class Resource(Page):
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        max_length=500,
        related_name='+'
    )

    thumbnail = models.ForeignKey(
        'core.AffixImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        max_length=500,
        related_name='+'
    )

    date = models.DateField(blank=True, null=True)
    content = StreamField([
        ("authors", blocks.RichTextBlock(blank=True)),
        ("copyright", blocks.RichTextBlock(blank=True)),
        ("focus", blocks.RichTextBlock(blank=True)),
        ("factoids", blocks.RichTextBlock(blank=True)),
    ])

    categories = ParentalManyToManyField("category.Category",
                          related_name="resources_by_category", blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    tags = ClusterTaggableManager(through=ResourceTag, blank=True)
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True, boost=SearchBoost.TITLE),
        index.SearchField('language'),
        index.SearchField('content', partial_match=True, boost=SearchBoost.CONTENT),
        index.FilterField('date'),
        index.FilterField('get_categories'),
        index.FilterField('language'),
        index.FilterField('get_search_type'),
    ]

    def get_search_type(self):
        return self.__class__.__name__.lower()

    def get_categories(self):
        return [category.name for category in self.categories.all()]

    def get_absolute_url(self):
        return reverse("resource-detail", kwargs={"slug": self.slug})

    def get_template(self, request, *args, **kwargs):
        self.template = "resources/resource_detail.html"
        return super(Resource, self).get_template(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        return {
            'resource': self,
            'request': request
        }

    content_panels = Page.content_panels + [
        DocumentChooserPanel('document'),
        ImageChooserPanel('thumbnail'),
        FieldPanel('language'),
        StreamFieldPanel('content'),
        FieldPanel('categories'),
        FieldPanel('date'),
    ]

    def clean(self):
        super(Resource, self).clean()

    @property
    def featured_image(self):
        return None

    def __str__(self):
        return self.title
