import datetime

from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.utils.translation import activate, deactivate_all
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.rich_text import RichText

from pari import settings


def get_translations_for_page(page):
    translations = []
    deactivate_all()
    if settings.ENABLE_SITE_LOCALIZATION:
        activate(settings.LANGUAGE_CODE)
    else:
        activate(page.language)

    try:
        trans_holder = page.get_children().get(title="Translations")
        if page.live:
            translations.append(page.specific)
        translations.extend(trans_holder.get_children().live().specific())
    except Page.DoesNotExist:
        # Check if page exists within the translation folder
        parent = page.get_parent()
        if parent.title == "Translations":
            if parent.get_parent().live:
                translations.append(parent.get_parent().specific)
            live_children = parent.get_children().live()
            if live_children:
                translations.extend(live_children.specific())
    return translations


def filter_by_language(request, *items_to_filter):
    lang = settings.LANGUAGE_CODE if settings.ENABLE_SITE_LOCALIZATION else 'en'
    filtered_list = []
    if request.GET.get("lang"):
        lang = request.GET["lang"]
    if not lang == 'all':
        for item in items_to_filter:
            filtered_list.append(item.filter(language=lang))
    return tuple(items_to_filter) if len(filtered_list) == 0 else tuple(filtered_list)


def get_translations_for_articles(articles):
    article_translations = {}
    for article in articles:
        article_translations[article] = get_translations_for_page(article)
    return article_translations


def get_unique_photographers(album):
    photographers = []
    for slide in album.slides.all():
        photographers.extend(slide.image.photographers.all())
    return set(photographers)


def get_slide_detail(album):
    response_data = {}
    response_data['slides'] = []
    photographers = []
    slide_photo_graphers = []
    for slide in album.slides.all():
        slide_photo_graphers.extend(map(lambda photographer_name: photographer_name.name.encode('UTF-8'),
                                        slide.image.photographers.all()))
    photographers_of_album = list(set(slide_photo_graphers))
    for index, slide in enumerate(album.slides.all(), start=0):
        slide_dict = dict([('type', 'image'), ('show_title', "True"), ('album_title', album.title)])
        slide_dict['src'] = slide.image.file.url
        slide_dict['src_resized'] = slide.image.get_rendition('height-876').url
        block = blocks.RichTextBlock()
        description_value = RichText(slide.description)
        slide_dict['description'] = block.render(description_value)
        slide_dict['album_description'] = album.description
        slide_dict['url'] = album.get_absolute_url()
        slide_dict['slide_photographer'] = map(lambda photographer_name: photographer_name.name.encode('UTF-8'),
                                               slide.image.photographers.all())
        if index == 0:
            slide_dict['slide_photographer'] = photographers_of_album
            print index
        photographers.extend(set(slide.image.photographers.all()))
        if album.first_published_at:
            published_date = datetime.datetime.strptime(str(album.first_published_at)[:10], "%Y-%m-%d")
        else:
            published_date = datetime.datetime.now()
        date = published_date.strftime('%d %b,%Y')
        slide_dict['image_captured_date'] = date
        image_location = slide.image.locations.first()
        slide_dict['slide_location'] = "%s, %s" % (
        image_location.district, image_location.state) if image_location else ''
        slide_dict['track_id'] = slide.audio
        response_data['slides'].append(slide_dict)

    response_data['authors'] = []
    for photographer in set(photographers):
        photographer_dict = dict(
            [('type', 'inline'), ('show_title', "False"), ('name', photographer.name), ('bio', photographer.bio_en),
             ('twitter_username', photographer.twitter_handle), ('facebook_username', photographer.facebook_username),
             ('email', photographer.email), ('website', photographer.website),
             ('author_url', reverse('author-detail', kwargs={'slug': photographer.slug}))])
        response_data['authors'].append(photographer_dict)
    return JsonResponse(response_data)


class SearchBoost(object):
    TITLE = 6
    AUTHOR = 5
    LOCATION = 4
    DESCRIPTION = 3
    CONTENT = 2
