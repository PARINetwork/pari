from django.utils.translation import activate, deactivate_all

from wagtail.wagtailcore.models import Page


def get_translations_for_page(page):
    translations = []
    deactivate_all()
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
    lang = 'en'
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