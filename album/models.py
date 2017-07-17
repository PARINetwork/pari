from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, \
    MultiFieldPanel, RichTextFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import M2MField, ParentalKey

from core.edit_handlers import M2MFieldPanel, AudioPanel
from core.utils import SearchBoost


@python_2_unicode_compatible
class Album(Page):
    description = RichTextField()
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    content_panels = Page.content_panels + [
        FieldPanel('language'),
        FieldPanel('description'),
        InlinePanel('slides', label=_('Slides'), panels=[
            ImageChooserPanel('image'),
            AudioPanel('audio'),
            RichTextFieldPanel('description')
        ]),
    ]

    template = "album/album_detail.html"

    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True, boost=SearchBoost.TITLE),
        index.SearchField('description', partial_match=True, boost=SearchBoost.DESCRIPTION),
        index.FilterField('language'),
        index.SearchField('get_locations_index', partial_match=True, boost=SearchBoost.LOCATION),
        index.SearchField('get_photographers_index', partial_match=True, boost=SearchBoost.AUTHOR)
    ]

    @property
    def locations(self):
        location_objects = []
        for slide in self.slides.filter(image__isnull=False):
            location_objects.extend(slide.image.locations.all())
        return set(location_objects)

    @property
    def photographers(self):
        photographer_objects = []
        for slide in self.slides.filter(image__isnull=False):
            photographer_objects.extend(slide.image.photographers.all())
        return set(photographer_objects)

    def get_locations_index(self):
        locations_index = map(lambda slide: slide.image.get_locations_index(), self.slides.filter(image__isnull=False))
        return " ".join(locations_index)

    def get_photographers_index(self):
        photographers_index = map(lambda slide: slide.image.get_all_photographers(), self.slides.filter(image__isnull=False))
        return " ".join(photographers_index)

    def get_context(self, request, *args, **kwargs):
        return {
            'album': self,
            'request': request
        }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        name = "album-detail"
        return reverse(name, kwargs={"slug": self.slug})

    @property
    def featured_image(self):
        return self.slides.all()[0].image


@python_2_unicode_compatible
class AlbumSlide(Orderable):
    page = ParentalKey("album.Album", related_name="slides")
    image = models.ForeignKey("core.AffixImage", related_name="album_for_image", null=True, blank=True)
    audio = models.CharField(blank=True, max_length=50)
    description = RichTextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "created_on"]

    def __str__(self):
        if self.image:
            return self.image.title
        return self.description
