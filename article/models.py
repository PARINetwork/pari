from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.core import serializers
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from elasticsearch import ConnectionError

from modelcluster.fields import M2MField
from wagtail.wagtailadmin import blocks

from wagtail.wagtailcore.models import Page, Site
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, \
    MultiFieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsearch.backends import get_search_backend
from wagtail.wagtailsearch.backends.elasticsearch import ElasticSearchMapping, \
    ElasticSearchResults

from article.streamfields.blocks import FullWidthImageBlock, TwoColumnImageBlock, ParagraphBlock, \
    ParagraphWithImageBlock, FaceBlock, ParagraphWithBlockQuoteBlock, NColumnParagraphBlock, FullWidthBlockQuote, \
    ParagraphWithEmbedBlock, ParagraphWithRawEmbedBlock, VideoWithQuoteBlock

from core.edit_handlers import M2MFieldPanel

# Override the url property of the Page model
# to accommodate for child pages
from core.utils import get_translations_for_page, SearchBoost

Page.wg_url = Page.url


@cached_property
def url_property(self):
    instance = self.specific
    if getattr(instance, 'get_absolute_url', None):
        return instance.get_absolute_url()
    return self.wg_url


Page.url = url_property


@python_2_unicode_compatible
class Article(Page):
    authors = M2MField("author.Author", related_name="articles_by_author")
    translators = M2MField("author.Author",
                           related_name="translations_by_author",
                           blank=True)
    strap = models.TextField(blank=True)
    content = RichTextField()
    modular_content = StreamField([
        ('full_width_image', FullWidthImageBlock()),
        ('n_column_paragraph_block', NColumnParagraphBlock()),
        ('two_column_image', TwoColumnImageBlock()),
        ('paragraph', ParagraphBlock()),
        ('paragraph_with_image', ParagraphWithImageBlock()),
        ('face', FaceBlock()),
        ('paragraph_with_block_quote', ParagraphWithBlockQuoteBlock()),
        ('full_width_block_quote', FullWidthBlockQuote()),
        ('paragraph_with_embed', ParagraphWithEmbedBlock()),
        ('paragraph_with_raw_embed', ParagraphWithRawEmbedBlock()),
        ('video_with_quote', VideoWithQuoteBlock()),
    ], null=True, blank=True)
    show_modular_content = models.BooleanField(default=False)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)
    original_published_date = models.DateField(null=True, blank=True)
    show_day = models.BooleanField(default=True)
    show_month = models.BooleanField(default=True)
    show_year = models.BooleanField(default=True)
    featured_image = models.ForeignKey('core.AffixImage',
                                       null=True, blank=True,
                                       on_delete=models.SET_NULL)
    show_featured_image = models.BooleanField(default=True)

    categories = M2MField("category.Category", related_name="articles_by_category")
    locations = M2MField("location.Location", related_name="articles_by_location", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('strap'),
        M2MFieldPanel('authors'),
        M2MFieldPanel('translators'),
        FieldPanel('language'),
        MultiFieldPanel(
            [
                FieldPanel('original_published_date'),
                FieldRowPanel(
                    [
                        FieldPanel('show_day',classname="col4"),
                        FieldPanel('show_month',classname="col4"),
                        FieldPanel('show_year',classname="col4")
                    ])
            ],'Date'),
        FieldPanel('content'),
        MultiFieldPanel(
            [
                ImageChooserPanel('featured_image'),
                FieldPanel('show_featured_image'),
            ], 'Cover Image'),
        FieldPanel('categories'),
        M2MFieldPanel('locations'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True, boost=SearchBoost.TITLE),
        index.SearchField('get_authors', partial_match=True, boost=SearchBoost.AUTHOR),
        index.SearchField('translators', partial_match=True, boost=SearchBoost.AUTHOR),
        index.SearchField('strap', partial_match=True, boost=SearchBoost.DESCRIPTION),
        index.SearchField('content', partial_match=True, boost=SearchBoost.CONTENT),
        index.SearchField('modular_content', partial_match=True, boost=SearchBoost.CONTENT),
        index.SearchField('get_district_from_location', partial_match=True, boost=SearchBoost.LOCATION),
        index.SearchField('language', partial_match=True),
        index.FilterField('categories'),
        index.FilterField('language'),
        index.FilterField('get_search_type'),
        index.FilterField('get_categories')
    ]

    def __str__(self):
        return self.title

    def get_authors(self):
        return [author.name for author in self.authors.all()]

    def get_district_from_location(self):
        return [location.address for location in self.locations.all()]

    def get_context(self, request, *args, **kwargs):
        try:
            site = Site.objects.get(hostname=request.get_host())
        except Site.DoesNotExist:
            site = Site.objects.filter(is_default_site=True)[0]
        return {
            'article': self,
            'request': request,
            'site': site
        }

    def get_absolute_url(self):
        name = "article-detail"
        return reverse(name, kwargs={"slug": self.slug})

    def get_translation(self):
        return get_translations_for_page(self)

    # Elastic search related methods
    def get_search_type(self):
        categories = [category.name for category in self.categories.all()]

        if 'VideoZone' in categories:
            return 'video'
        elif 'AudioZone' in categories:
            return 'audio'
        else:
            return 'article'

    def get_categories(self):
        return [category.name for category in self.categories.all()]

    def related_articles(self):
        if not self.pk:
            # In preview mode
            return []

        lookup_fields = ['authors', 'translators', 'locations']
        higher_boost = 2
        max_results = getattr(settings, "MAX_RELATED_RESULTS", 4)

        es_backend = get_search_backend()
        mapping = ElasticSearchMapping(self.__class__)
        search_fields = []

        for ii in self.search_fields:
            if ii.field_name in lookup_fields:
                search_fields.append("{0}^{1}".format(ii.field_name, higher_boost))
            else:
                search_fields.append(ii.field_name)
        query = {
            "query": {
                "filtered": {
                    "filter": {
                        "term": {
                            "live_filter": True
                        }
                    },
                    "query": {
                        "more_like_this": {
                            "docs": [
                                {
                                    "_id": mapping.get_document_id(self),
                                    "_type": mapping.get_document_type()
                                }
                            ],
                            "min_doc_freq": 1,
                            "min_term_freq": 2,
                            "max_query_terms": 500,
                            "min_word_length": 4,
                            "fields": search_fields
                        }
                    }
                }
            }
        }

        try:
            mlt = es_backend.es.search(
                index=es_backend.index_name,
                doc_type=mapping.get_document_type(),
                body=query
            )
        except ConnectionError:
            return []
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


if settings.MODULAR_ARTICLE:
    Article.content_panels.insert(-4, MultiFieldPanel([FieldPanel('show_modular_content')],
                                                      'Want to show modular content ?'))
    Article.content_panels.insert(-5, StreamFieldPanel('modular_content'))
