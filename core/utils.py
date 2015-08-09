from django.utils.translation import activate

from wagtail.wagtailcore.models import Page


def get_translations_for_page(page):
    translations = []
    if page.language != "en":
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
