from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    StreamFieldPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalManyToManyField

from core.utils import SearchBoost


@python_2_unicode_compatible
class Resource(Page):
    date = models.DateField(blank=True, null=True)
    content = StreamField([
        ("authors", blocks.RichTextBlock(blank=True)),
        ("copyright", blocks.RichTextBlock(blank=True)),
        ("focus", blocks.RichTextBlock(blank=True)),
        ("factoids", blocks.RichTextBlock(blank=True)),
    ])
    embed_url = models.URLField()
    embed_thumbnail = models.TextField(blank=True, null=True)
    categories = ParentalManyToManyField("category.Category",
                          related_name="resources_by_category")
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True, boost=SearchBoost.TITLE),
        index.SearchField('language'),
        index.SearchField('content', partial_match=True, boost=SearchBoost.CONTENT),
        index.FilterField('date'),
        index.FilterField('categories'),
        index.FilterField('language'),
        index.FilterField('get_search_type'),
    ]

    def get_search_type(self):
        return self.__class__.__name__.lower()

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
        FieldPanel('language'),
        FieldPanel('embed_url'),
        FieldPanel('embed_thumbnail'),
        StreamFieldPanel('content'),
        FieldPanel('categories'),
        FieldPanel('date'),
    ]

    @property
    def featured_image(self):
        return None

    def __str__(self):
        return self.title
