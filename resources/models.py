from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
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


class Room(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255,
                            help_text=_('Auto-populated field. Edit manually only if you must'))
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Rack(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            help_text=_('Auto-populated field. Edit manually only if you must'))
    room = models.ForeignKey('Room', related_name='racks')

    class Meta:
        unique_together = (('name', 'room'), ('slug', 'room'))
        ordering = ('id',)

    def __str__(self):
        return self.room.name + ' > ' + self.name


class Subject(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255,
                            help_text=_('Auto-populated field. Edit manually only if you must'))

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class ResourceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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

    rooms = ParentalManyToManyField('resources.Room',
                                    related_name='resources')
    racks = ParentalManyToManyField('resources.Rack',
                                    related_name='resources')

    subjects = ParentalManyToManyField('resources.Subject',
                                       related_name='resources',
                                       blank=True)

    type = models.ForeignKey('resources.ResourceType',
                             related_name='resources',
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL)

    categories = ParentalManyToManyField("category.Category",
                                         related_name="resources_by_category",
                                         blank=True)
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
        FieldPanel('racks'),
        FieldPanel('subjects'),
        FieldPanel('type'),
        FieldPanel('categories'),
        FieldPanel('date'),
    ]

    def clean(self):
        super(Resource, self).clean()

    def save(self, *args, **kwargs):
        rooms = set([x.room for x in self.racks.all()])
        for room in rooms:
            self.rooms.add(room)
        super(Resource, self).save()

    @property
    def featured_image(self):
        return None

    def __str__(self):
        return self.title
