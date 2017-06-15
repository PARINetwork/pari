from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, \
    StreamFieldPanel, PageChooserPanel, FieldPanel
from wagtail.wagtailadmin.forms import WagtailAdminPageForm
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.formats import get_image_format
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.blocks import ImageChooserBlock

from album.models import Album
from article.models import Article
from category.models import Category
from core.utils import get_translations_for_page


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


class FeaturedSectionBlock(StructBlock):
    title = blocks.CharBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    url = blocks.CharBlock()
    featured_image = ImageChooserBlock()
    featured_image_label = blocks.CharBlock(required=False)


class HomePageAdminMediaForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super(HomePageAdminMediaForm, self).__init__(*args, **kwargs)
        self.fields['talking_album'] = forms.CharField(max_length=50,
                                                       widget=forms.Select(
                                                           choices=Album.objects.live().filter(
                                                               ~Q(slides__audio='')).distinct().values_list(
                                                               'page_ptr_id', 'title')))
        self.fields['photo_album'] = forms.CharField(max_length=50,
                                                     widget=forms.Select(choices=Album.objects.live().filter(
                                                         Q(slides__audio='')).distinct().values_list('page_ptr_id',
                                                                                                     'title')))
        self.fields['video'] = forms.CharField(max_length=50,
                                               widget=forms.Select(choices=Article.objects.live().filter(
                                                   Q(categories__name='VideoZone')).values_list('page_ptr_id',
                                                                                                'title')))

    def clean_talking_album(self):
        talking_album = Album.objects.get(page_ptr_id=self.cleaned_data['talking_album'])
        return talking_album

    def clean_photo_album(self):
        photo_album = Album.objects.get(page_ptr_id=self.cleaned_data['photo_album'])
        return photo_album

    def clean_video(self):
        video = Article.objects.get(page_ptr_id=self.cleaned_data['video'])
        return video


class HomePageAdminForm(HomePageAdminMediaForm):
    in_focus_title = forms.CharField(required=True)
    in_focus_link = forms.CharField(required=True)
    in_focus_link_text = forms.CharField(required=True)

    def clean_in_focus_page1(self):
        page1 = self.cleaned_data['in_focus_page1']
        if not page1:
            raise forms.ValidationError(_('Please add a page'))
        return page1

    def clean_in_focus_page2(self):
        page2 = self.cleaned_data['in_focus_page2']
        if not page2:
            raise forms.ValidationError(_('Please add a page'))
        return page2


@python_2_unicode_compatible
class HomePage(Page):
    featured_content = StreamField([
        ("featured_section", FeaturedSectionBlock()),
    ], blank=True, null=True)

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
    in_focus_title = models.TextField(blank=True, null=True, verbose_name="Title")
    in_focus_link = models.TextField(blank=True, null=True, verbose_name="Link")
    in_focus_link_text = models.TextField(blank=True, null=True, verbose_name="Link Text")
    in_focus_page1 = models.ForeignKey("wagtailcore.Page",
                                       null=True, blank=True,
                                       on_delete=models.PROTECT,
                                       related_name="+", verbose_name="Page one")
    in_focus_page2 = models.ForeignKey("wagtailcore.Page",
                                       null=True, blank=True,
                                       on_delete=models.PROTECT,
                                       related_name="+", verbose_name="Page two")

    talking_album = models.ForeignKey("album.Album",
                                      null=True, blank=True, related_name='+', on_delete=models.PROTECT)
    photo_album = models.ForeignKey("album.Album",
                                    null=True, blank=True, related_name='+', on_delete=models.PROTECT)
    video = models.ForeignKey("article.Article",
                              null=True, blank=True, on_delete=models.PROTECT)

    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    content_panels = Page.content_panels + [
        MultiFieldPanel([StreamFieldPanel('featured_content')], heading="Featured Content", classname="collapsible "),
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
        MultiFieldPanel([
            FieldPanel('in_focus_title'),
            FieldPanel('in_focus_link'),
            FieldPanel('in_focus_link_text'),
            PageChooserPanel('in_focus_page1'),
            PageChooserPanel('in_focus_page2'),
        ], "In Focus"),
        FieldPanel('talking_album'),
        FieldPanel('photo_album'),
        FieldPanel('video'),
        FieldPanel('language'),
    ]

    base_form_class = HomePageAdminForm

    def __str__(self):
        return _("HomePage")

    def get_context(self, request, *args, **kwargs):
        category1 = Category.objects.get(slug="resource-conflicts")
        category2 = Category.objects.get(slug="adivasis")
        category3 = Category.objects.get(slug="dalits")
        category4 = Category.objects.get(slug="sports-games")
        return {
            'talking_album': {
                'image': self.talking_album.slides.first().image,
                'count': self.talking_album.slides.count(),
                'photographers': self.talking_album.photographers,
                'section_model': self.talking_album,
            },
            'photo_album': {
                'image': self.photo_album.slides.first().image,
                'count': self.photo_album.slides.count(),
                'photographers': self.photo_album.photographers,
                'section_model': self.photo_album,
            },
            'video': {
                'image': self.video.featured_image,
                'photographers': self.video.authors.all(),
                'section_model': self.video,
            },
            'page': self,
            'categories': [category1, category2, category3, category4],
            'translations': get_translations_for_page(self),
            'translations_for_infocus_article1': get_translations_for_page(self.in_focus_page1.specific),
            'translations_for_infocus_article2': get_translations_for_page(self.in_focus_page2.specific),
            'current_page': 'home-page',
            'request': request,
            'categories': [category1, category2, category3, category4]
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


class SubSectionBlock(StructBlock):
    heading = blocks.CharBlock()
    content = blocks.RichTextBlock()


@python_2_unicode_compatible
class GuidelinesPage(Page):
    strap = models.TextField(blank=True)
    content = StreamField([
        ("heading_title", blocks.CharBlock()),
        ("heading_content", blocks.RichTextBlock()),
        ("sub_section_with_heading", SubSectionBlock()),
        ("sub_section_without_heading", blocks.RichTextBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('strap'),
        MultiFieldPanel([StreamFieldPanel('content')], heading="Content", classname="collapsible "),
    ]

    def __str__(self):
        return _("GuidelinesPage")


class GalleryHomePageAdminForm(HomePageAdminMediaForm):
    photo_title = forms.CharField(required=True)
    photo_link = forms.CharField(required=False)

    def clean_photo_of_the_week(self):
        photo_of_the_week = self.cleaned_data["photo_of_the_week"]
        if photo_of_the_week and photo_of_the_week.photographers.count() == 0:
            raise forms.ValidationError(_('Please add photographers to the image'))
        return self.cleaned_data["photo_of_the_week"]


@python_2_unicode_compatible
class GalleryHomePage(Page):
    photo_of_the_week = models.ForeignKey("core.AffixImage", null=False, blank=False, on_delete=models.PROTECT)
    photo_title = models.TextField(blank=False, null=False)
    photo_link = models.TextField(blank=True, null=True)
    talking_album = models.ForeignKey("album.Album",
                                      null=False, blank=False, related_name='talking', on_delete=models.PROTECT)
    photo_album = models.ForeignKey("album.Album",
                                    null=False, blank=False, related_name='photo', on_delete=models.PROTECT)
    video = models.ForeignKey("article.Article",
                              null=False, blank=False, on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('photo_of_the_week'),
            FieldPanel('photo_title'),
            FieldPanel('photo_link'),
        ]),
        FieldPanel('talking_album'),
        FieldPanel('photo_album'),
        FieldPanel('video'),
    ]

    base_form_class = GalleryHomePageAdminForm

    def __str__(self):
        return _("GalleryHomePage")


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
    date = models.DateTimeField(null=True, blank=True, verbose_name="captured date")
    camera = models.CharField(max_length=50, null=True, blank=True)

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
        index.FilterField('get_all_photographers'),
    )

    def get_all_photographers(self):
        photographers = []
        for photographer in self.photographers.all():
            photographers.append(" ".join([photographer.name or ""]))
        return " ".join(photographers)

    def get_locations_index(self):
        locations = []
        for location in self.locations.all():
            locations.append(" ".join([location.name or "",
                                       location.sub_district_name or "",
                                       location.district or "",
                                       location.region or "",
                                       location.state or ""]))
        return " ".join(locations)

    def get_categories_index(self):
        return [category.pk for category in self.categories.all()]

    @property
    def alt_text(self):
        return self.event

    @property
    def default_alt_text(self):
        return self.alt_text


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
