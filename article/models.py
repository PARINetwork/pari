from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
from django.conf import settings
from django.core.urlresolvers import reverse

from modelcluster.fields import M2MField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsearch.backends import get_search_backend
from wagtail.wagtailsearch.backends.elasticsearch import ElasticSearchMapping, \
    ElasticSearchResults

from core.edit_handlers import M2MFieldPanel


class Article(Page):
    authors = M2MField("author.Author", related_name="articles_by_author")
    strap = models.TextField(blank=True)
    content = RichTextField()
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)
    original_published_date = models.DateField(null=True, blank=True)
    featured_image = models.ForeignKey('core.AffixImage',
                                       null=True, blank=True,
                                       on_delete=models.SET_NULL)
    categories = M2MField("category.Category", related_name="articles_by_category")
    locations  = M2MField("location.Location", related_name="articles_by_location")

    content_panels = Page.content_panels + [
        FieldPanel('strap'),
        M2MFieldPanel('authors'),
        FieldPanel('language'),
        FieldPanel('original_published_date'),
        FieldPanel('content'),
        ImageChooserPanel('featured_image'),
        FieldPanel('categories'),
        M2MFieldPanel('locations'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('authors', partial_match=True),
        index.SearchField('strap', partial_match=True, boost=2),
        index.SearchField('content', partial_match=True, boost=2),
        index.FilterField('categories'),
        index.SearchField('locations', partial_match=True),
        index.FilterField('language'),
    )

    def get_context(self, request, *args, **kwargs):
        return {
            'article': self,
            'request': request
        }

    def get_absolute_url(self):
        name = "article-detail"
        return reverse(name, kwargs={"slug": self.slug})

    def related_articles(self):
        if not self.pk:
            # In preview mode
            return []
        max_results = getattr(settings, "MAX_RELATED_RESULTS", 4)
        es_backend = get_search_backend()
        mapping = ElasticSearchMapping(self.__class__)
        mlt = es_backend.es.mlt(es_backend.es_index,
                                mapping.get_document_type(),
                                mapping.get_document_id(self),
                                params={"fields": self.search_fields})
        # Get pks from results
        pks = [hit['_source']['pk'] for hit in mlt['hits']['hits']][:max_results]

        # Initialise results dictionary
        results = dict((str(pk), None) for pk in pks)

        # Find objects in database and add them to dict
        queryset = self._default_manager.filter(pk__in=pks)
        for obj in queryset:
            results[str(obj.pk)] = obj

        # Return results in order given by ElasticSearch
        return [results[str(pk)] for pk in pks if results[str(pk)]]
