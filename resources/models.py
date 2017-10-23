from __future__ import unicode_literals

import json
import urllib2

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

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
    url = models.URLField(blank=True,null=True)
    embed_url = models.URLField()
    embed_thumbnail = models.TextField(blank=True, null=True)
    categories = ParentalManyToManyField("category.Category",
                          related_name="resources_by_category", blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

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
        FieldPanel('language'),
        FieldPanel('url'),
        FieldPanel('embed_url'),
        FieldPanel('embed_thumbnail'),
        StreamFieldPanel('content'),
        FieldPanel('categories'),
        FieldPanel('date'),
    ]

    def clean(self):
        if self.url and self.url == self.embed_url:
            slideshare_api = "https://www.slideshare.net/api/oembed/2/?url=" + self.url + '&format=json'
            try:
                data_from_slideshare = urllib2.urlopen(slideshare_api).read()
            except:
                raise ValidationError({'url': "This Url is not a Valid SlideShare Url"})
            data = json.loads(data_from_slideshare)

            slideshare_embed_url = 'https://www.slideshare.net/slideshow/embed_code/' + str(data['slideshow_id']) + '/'

            self.embed_url = slideshare_embed_url
            self.embed_thumbnail = data['thumbnail'].replace('.jpg?cb=',
                                                             '-4.jpg?cb=')  # the "-4" before jpg is for high resolution thumbnail image

        super(Resource, self).clean()

    @property
    def featured_image(self):
        return None

    def __str__(self):
        return self.title
