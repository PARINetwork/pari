from __future__ import absolute_import, unicode_literals

from django.contrib.messages import success
from django.db.models import Max
from django.http import Http404
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _, activate, get_language
from django.views.decorators.cache import cache_page
from wagtail.wagtailadmin.views.pages import PreviewOnEdit, PreviewOnCreate
from wagtail.wagtailcore.models import Page, Site

from category.models import Category
from core.utils import get_translations_for_page, construct_guidelines
from .forms import ContactForm
from .models import HomePage, GuidelinesPage


def home_page(request, slug="home-page"):
    home_page = HomePage.objects.get(slug=slug)
    translations = get_translations_for_page(home_page)
    video = home_page.video
    talking_album = home_page.talking_album
    photo_album = home_page.photo_album
    category1 = Category.objects.get(slug="resource-conflicts")
    category2 = Category.objects.get(slug="adivasis")
    category3 = Category.objects.get(slug="dalits")
    category4 = Category.objects.get(slug="sports-games")
    home_context = {
        'talking_album': {
            'image': talking_album.slides.first().image,
            'count': talking_album.slides.count(),
            'photographers': get_unique_photographers(talking_album),
            'section_model': talking_album,
        },
        'photo_album': {
            'image': photo_album.slides.first().image,
            'count': photo_album.slides.count(),
            'photographers': get_unique_photographers(photo_album),
            'section_model': photo_album,
        },
        'video': {
            'image': video.featured_image,
            'photographers': video.authors.all(),
            'section_model': video,
        },
        "page": home_page,
        "categories": [category1, category2, category3, category4],
        "translations": translations,
        "translations_for_infocus_article1": get_translations_for_page(home_page.in_focus_page1.specific),
        "translations_for_infocus_article2": get_translations_for_page(home_page.in_focus_page2.specific),
        "current_page": 'home-page',
    }
    return render(request, "core/home_page.html", home_context)


def get_unique_photographers(talking_album):
    photographers = []
    for slide in talking_album.slides.all():
        photographers.extend(slide.image.photographers.all())
    return set(photographers)


def static_page(request, slug=None):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404
    if page.specific_class == HomePage:
        return home_page(request, page.slug)
    active_tab = 'about-pari'
    if 'donate' in slug:
        active_tab = 'donate'
    translations = get_translations_for_page(page.specific)
    return render(request, "core/static_page.html", {
        "self": page.specific,
        "translations": translations,
        "tab": active_tab,
        "current_page": slug,
    })


def guidelines(request):
    guideline = GuidelinesPage.objects.first()
    page_content = construct_guidelines(guideline.content)
    active_tab = 'about-pari'
    return render(request, "core/guidelines.html", {
        "page": guideline,
        "page_content": page_content,
        "tab": active_tab,
    })


def contribute_to_faces(request, slug=None):
    active_tab = 'about-pari'
    link = 'https://script.google.com/macros/s/AKfycbzMQwyY8P1t7CT0_ylmPfSDz7WiSTVHWtL-Yf0UhtoYOIWQfMf5/exec'
    return render(request, "core/contribute-to-faces.html",
                  {"tab": active_tab,
                   "link": link,
                   "current_page": 'contribute_to_faces',
                   })


def acknowledgements(request, slug=None):
    active_tab = 'about-pari'
    link = 'https://script.google.com/macros/s/AKfycbzMQwyY8P1t7CT0_ylmPfSDz7WiSTVHWtL-Yf0UhtoYOIWQfMf5/exec'
    return render(request, "core/acknowledgements.html",
                  {"tab": active_tab,
                   "link": link,
                   "current_page": 'acknowledgements',
                   })


def donate(request):
    return render(request, "core/donate.html", {"tab": "donate", "current_page": 'donate'})


def about(request):
    return render(request, "core/about.html", {"tab": "about-pari", "current_page": 'about'})


def founders(request):
    return render(request, "core/founders.html", {"tab": "about-pari", "current_page": 'founders'})


def pari_teachers_students(request):
    active_tab = 'about-pari'
    return render(request, "core/pari_teachers_students.html", {
        "tab": active_tab,
        "current_page": 'pari_teachers_students',
    })


def contribute(request, slug=None):
    return render(request, "core/contribute.html", {
        "tab": 'about-pari',
        "current_page": 'contribute',
    })


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, _("Your query has successfully been sent"))
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "core/contact_us.html", {
        "contact_form": form,
        "tab": "about-pari",
        "current_page": 'contact_us',
    })


class ModelTranslatedPagePreviewMixin(object):
    def get(self, request, *args, **kwargs):
        curr_lang = get_language()
        response = super(ModelTranslatedPagePreviewMixin, self).get(request, *args, **kwargs)

        post_data_dict, timestamp = self.request.session[self.session_key]
        language = post_data_dict.get('language')
        if language:
            activate(language[0])
        else:
            activate(curr_lang)

        return response


class PreviewOnEditPage(ModelTranslatedPagePreviewMixin, PreviewOnEdit):
    pass


class PreviewOnCreatePage(ModelTranslatedPagePreviewMixin, PreviewOnCreate):
    pass


@cache_page(86400)
def sitemap_index(request):
    site = Site.objects.get(hostname=request.get_host())
    pages = Page.objects.filter(live=True).exclude(title="Translations")
    years = pages.datetimes("first_published_at", "year") \
        .order_by("-datetimefield")
    last_upd = []
    for year in years:
        last_upd.append(pages.filter(first_published_at__year=year.year) \
                        .aggregate(dt=Max("latest_revision_created_at")))
    return render(request, "sitemaps/sitemap.xml", {
        "site": site,
        "years": zip(years, last_upd)
    }, content_type="text/xml")


@cache_page(86400)
def sitemap_year(request, year=None):
    site = Site.objects.get(hostname=request.get_host())
    pages = Page.objects.filter(live=True).exclude(title="Translations")
    pages = pages.filter(first_published_at__year=year)
    return render(request, "sitemaps/sitemap-year.xml", {
        "site": site,
        "pages": pages
    }, content_type="text/xml")
