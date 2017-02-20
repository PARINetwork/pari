from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailimages.models import AbstractImage, AbstractRendition
from wagtail.wagtailimages.formats import get_image_format
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, \
    StreamFieldPanel, PageChooserPanel, FieldPanel
from wagtail.wagtailsearch import index


@python_2_unicode_compatible
class StaticPage(Page):
    # TODO: Keep it simple for now.
    content = RichTextField(blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    def __str__(self):
        return self.title

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('language'),
    ]

    def get_absolute_url(self):
        return reverse("static_page", kwargs={"slug": self.slug})


@python_2_unicode_compatible
class HomePage(Page):
    # TODO: Carousel is temporary and being phased out
    carousel_0 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_1 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_2 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_3 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_4 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_5 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_6 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_7 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_8 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")
    carousel_9 = models.ForeignKey("wagtailcore.Page",
                                   null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="+")

    announcements = RichTextField(blank=True)

    strap = StreamField([
        ("tagline_1", blocks.RichTextBlock()),
        ("tagline_2", blocks.RichTextBlock()),
    ])
    about = StreamField([
        ("column_1", blocks.RichTextBlock()),
        ("column_2", blocks.RichTextBlock()),
        ("column_3", blocks.RichTextBlock()),
        ("column_4", blocks.RichTextBlock()),
    ])
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    content_panels = Page.content_panels + [
        StreamFieldPanel('strap'),
        FieldPanel('announcements'),
        MultiFieldPanel([
            PageChooserPanel('carousel_0'),
            PageChooserPanel('carousel_1'),
            PageChooserPanel('carousel_2'),
            PageChooserPanel('carousel_3'),
            PageChooserPanel('carousel_4'),
            PageChooserPanel('carousel_5'),
            PageChooserPanel('carousel_6'),
            PageChooserPanel('carousel_7'),
            PageChooserPanel('carousel_8'),
            PageChooserPanel('carousel_9'),
        ], "Carousel"),
        StreamFieldPanel('about'),
        FieldPanel('language'),
    ]

    def __str__(self):
        return _("HomePage")

    def get_context(self, request, *args, **kwargs):
        return {
            'page': self,
            'request': request,
            'announcements': self.announcements
        }

    def carousel(self):
        items = []
        for ii in range(10):
            item = getattr(self, "carousel_{0}".format(ii))
            if item:
                items.append(item)
        return items

    def get_absolute_url(self):
        return reverse("home-page")


@python_2_unicode_compatible
class AffixImage(AbstractImage):
    locations = models.ManyToManyField('location.Location', blank=True,
                                       related_name="locations_for_image")
    photographers = models.ManyToManyField("author.Author",
                             related_name="images_of_photographer", blank=True)
    people = models.TextField(blank=True)
    event = models.TextField(blank=True)
    categories = models.ManyToManyField('category.Category', blank=True,
                                        related_name="categories_for_image")
    arrival_date = models.DateTimeField(null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    camera = models.CharField(max_length=50,null=True, blank=True)

    admin_form_fields = (
        'title',
        'file',
        'locations',
        'people',
        'photographers',
        'event',
        'categories',
        'date',
        'camera',
        'arrival_date',
        'published_date',
        'tags',
        'focal_point_x',
        'focal_point_y',
        'focal_point_width',
        'focal_point_height',
    )

    def __str__(self):
        return self.title

    search_fields = AbstractImage.search_fields + (
        index.SearchField('get_locations_index', partial_match=True),
        index.SearchField('people', partial_match=True),
        index.SearchField('event', partial_match=True),
        index.FilterField('get_categories_index'),
        index.FilterField('arrival_date'),
        index.FilterField('published_date'),
        index.FilterField('camera'),
    )

    def get_locations_index(self):
        locations = []
        for location in self.locations.all():
            locations.append(" ".join([location.name or "",
                                       location.block or "",
                                       location.district or "",
                                       location.region or "",
                                       location.state or ""]))
        return " ".join(locations)

    def get_categories_index(self):
        return [category.pk for category in self.categories.all()]


@python_2_unicode_compatible
class AffixImageRendition(AbstractRendition):
    image = models.ForeignKey(AffixImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )

    def img_tag(self, extra_attributes=''):
        fw_format = get_image_format("fullwidth")
        extra_attrs = extra_attributes or ''
        if fw_format.filter_spec == self.filter.spec:
            return fw_format.image_to_html(
                self.image, self.image.title, extra_attrs
            )
        return super(AffixImageRendition, self).img_tag(extra_attrs)

    def __str__(self):
        return self.image.title


@python_2_unicode_compatible
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
