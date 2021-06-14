from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.db import models
import django.db.models.deletion
from six import python_2_unicode_compatible
from django.utils.functional import cached_property
from elasticsearch import ConnectionError
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, \
    MultiFieldPanel, FieldRowPanel, StreamFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Site
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.search.backends import get_search_backend
from wagtail.search.backends.elasticsearch6 import Elasticsearch6Mapping

from article.streamfields.blocks import FullWidthImageBlock, ParagraphBlock, \
    ParagraphWithBlockQuoteBlock, NColumnParagraphBlock, FullWidthBlockQuote, \
    ParagraphWithEmbedBlock, ParagraphWithRawEmbedBlock, VideoWithQuoteBlock, FullWidthEmbedBlock, \
    ParagraphWithMapBlock, ImageWithQuoteAndParagraphBlock, ParagraphWithPageBlock, NColumnImageWithTextBlock
from core.edit_handlers import M2MFieldPanel
# Override the url property of the Page model
# to accommodate for child pages
from core.utils import get_translations_for_page, SearchBoost
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from core.widgets import JqueryChosenSelect
from collections import defaultdict

Page.wg_url = Page.url


@property
def url_property(self):
    instance = self.specific
    if getattr(instance, 'get_absolute_url', None):
        return instance.get_absolute_url()
    return self.wg_url


Page.url = url_property


class ArticleTag(TaggedItemBase):
    content_object = ParentalKey('article.Article', related_name='tagged_items')


class ArticleAuthors(models.Model):
    article = ParentalKey('article.Article', related_name='authors')
    author = models.ForeignKey('author.Author', related_name='articles_by_author', on_delete=django.db.models.deletion.PROTECT)
    role = models.ForeignKey('author.Role', related_name='author_credit', on_delete=django.db.models.deletion.PROTECT, null=True, blank=True)
    show_in_beginning = models.BooleanField(default=True)
    show_in_end = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    sort_order_field = 'sort_order'
    panels = [
        MultiFieldPanel([
            FieldPanel('author', widget=JqueryChosenSelect),
            FieldPanel('role', widget=JqueryChosenSelect),
            FieldRowPanel([
                FieldPanel('show_in_beginning'),
                FieldPanel('show_in_end')
            ])
        ])
    ]

    class Meta:
        db_table = 'article_article_authors'
        unique_together = ('article', 'author', 'role', 'sort_order')
        ordering = ('sort_order',)

    def __str__(self):
        return self.author.name


@python_2_unicode_compatible
class Article(Page):
    strap = models.TextField(blank=True)
    content = RichTextField(blank=True, verbose_name="Content - Deprecated. Use 'MODULAR CONTENT' instead.")
    modular_content = StreamField([
        ('paragraph', ParagraphBlock()),
        ('n_column_paragraph', NColumnParagraphBlock()),
        ('paragraph_with_map', ParagraphWithMapBlock()),
        ('paragraph_with_page', ParagraphWithPageBlock()),

        ('paragraph_with_quote', ParagraphWithBlockQuoteBlock()),
        ('full_width_quote', FullWidthBlockQuote()),
        ('video_with_quote', VideoWithQuoteBlock()),

        ('image_with_quote_and_paragraph', ImageWithQuoteAndParagraphBlock()),
        ('full_width_image', FullWidthImageBlock()),
        ('columnar_image_with_text', NColumnImageWithTextBlock()),

        ('full_width_embed', FullWidthEmbedBlock()),
        ('paragraph_with_embed', ParagraphWithEmbedBlock()),
        ('paragraph_with_raw_embed', ParagraphWithRawEmbedBlock()),

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

    categories = ParentalManyToManyField("category.Category", related_name="articles_by_category")
    locations = ParentalManyToManyField("location.Location", related_name="articles_by_location", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('strap'),
        InlinePanel('authors', label='Authors', min_num=1),
        FieldPanel('language'),
        MultiFieldPanel(
            [
                FieldPanel('original_published_date'),
                FieldRowPanel(
                    [
                        FieldPanel('show_day', classname="col4"),
                        FieldPanel('show_month', classname="col4"),
                        FieldPanel('show_year', classname="col4")
                    ])
            ], 'Date'),
        FieldPanel('content'),
        MultiFieldPanel(
            [
                ImageChooserPanel('featured_image'),
                FieldPanel('show_featured_image'),
            ], 'Cover Image'),
        FieldPanel('categories'),
        M2MFieldPanel('locations'),
    ]

    tags = ClusterTaggableManager(through=ArticleTag, blank=True)
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True, boost=SearchBoost.TITLE),
        index.SearchField('get_authors', partial_match=True, boost=SearchBoost.AUTHOR),
        index.SearchField('strap', partial_match=True, boost=SearchBoost.DESCRIPTION),
        index.SearchField('content', partial_match=True, boost=SearchBoost.CONTENT),
        index.SearchField('modular_content', partial_match=True, boost=SearchBoost.CONTENT),
        index.SearchField('get_district_from_location', partial_match=True, boost=SearchBoost.LOCATION),
        index.SearchField('language', partial_match=True),
        index.FilterField('language'),
        index.FilterField('get_search_type'),
        index.FilterField('get_categories'),
        index.FilterField('get_minimal_locations'),
        index.FilterField('get_authors_or_photographers'),
        index.FilterField('title'),
        index.FilterField('get_state_from_locations')
    ]

    def __str__(self):
        return self.title

    def get_authors(self):
        return [article_author.author.name for article_author in self.authors.all()]

    def get_author_role_map(self, **kwargs):
        authors_with_role = kwargs['authors_with_role']
        temp = defaultdict(list)
        for awr in authors_with_role:
            role = awr.role
            if role:
                temp[role.name].append(awr.author)
            else:
                temp['None'].append(awr.author)
        return dict((key, tuple(val)) for key, val in temp.items())

    def beginning_authors_with_role(self):
        return self.get_author_role_map(authors_with_role=self.authors.filter(show_in_beginning=True).all())

    def end_authors_with_role(self):
        return self.get_author_role_map(authors_with_role=self.authors.filter(show_in_end=True).all())

    def get_authors_or_photographers(self):
        return self.get_authors()

    def get_district_from_location(self):
        return [location.address for location in self.locations.all()]

    def get_minimal_locations(self):
        return [location.minimal_address for location in self.locations.all()]

    def get_state_from_locations(self):
        return [location.state for location in self.locations.all()]

    def get_context(self, request, *args, **kwargs):
        try:
            site = Site.objects.get(hostname=request.get_host())
        except Site.DoesNotExist:
            site = Site.objects.filter(is_default_site=True)[0]
        return {
            'article': self,
            'beginning_authors_with_role': self.beginning_authors_with_role(),
            'end_authors_with_role': self.end_authors_with_role(),
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

        max_results = getattr(settings, "MAX_RELATED_RESULTS", 4)
        es_backend = get_search_backend()
        mapping = Elasticsearch6Mapping(self.__class__)

        minimal_locations = ""
        if (self.get_minimal_locations()):
            minimal_locations = self.get_minimal_locations()

        state_locations = ""
        if (self.get_state_from_locations()):
            state_locations = self.get_state_from_locations()

        authors_of_article = ""

        if self.authors:
            authors_of_article = self.get_authors()

        query = {
            "track_scores": "true",
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "fields": ["*language_filter"],
                                "query":  self.language
                            }

                        },
                        {"term": {"live_filter": "true"}}
                    ],
                    "must_not": [
                        {"term": {"title_filter": self.title}}

                    ],
                    "should": [
                        {
                            "multi_match": {
                                "fields": ["*get_authors_or_photographers_filter"],
                                "query": ' '.join(authors_of_article),
                                "type": "cross_fields",
                                "operator": "or"
                            }

                        },
                        {
                            "multi_match": {
                                "fields": ["*get_authors"],
                                "query": ' '.join(authors_of_article),
                                "type": "cross_fields",
                                "operator": "or"
                            }

                        },
                        {
                            "multi_match": {
                                "fields": ["*get_minimal_locations_filter"],
                                "query": ' '.join(minimal_locations),
                                "type": "cross_fields",
                                "operator": "and"
                            }
                        },
                        {
                            "multi_match": {
                                "fields": ["*get_state_from_locations_filter"],
                                "query": ' '.join(state_locations),
                                "type": "cross_fields",
                                "operator": "and"
                            }

                        },
                        {
                            "match": {
                                "title": self.title
                            }
                        }
                    ],
                    "minimum_should_match": 1
                }
            },
            "sort": [
                {"_score": {"order": "desc"}},
                {"article_article__get_authors_or_photographers_filter": {"order": "desc"}},
                {"album_album__get_authors_or_photographers_filter": {"order": "desc"}},
                {"face_face__get_authors_or_photographers_filter": {"order": "desc"}},
                {"first_published_at_filter": "desc"}
            ]
        }

        try:
            mlt = es_backend.es.search(
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
        queryset = self._meta.default_manager.filter(pk__in=pks)
        for obj in queryset:
            results[str(obj.pk)] = obj

        # Return results in order given by ElasticSearch
        return [results[str(pk)] for pk in pks if results[str(pk)]]


if settings.MODULAR_ARTICLE:
    Article.content_panels.insert(-4, MultiFieldPanel([FieldPanel('show_modular_content')],
                                                      'Want to show modular content ?'))
    Article.content_panels.insert(-5, StreamFieldPanel('modular_content'))
