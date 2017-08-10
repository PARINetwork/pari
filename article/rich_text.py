from __future__ import absolute_import, unicode_literals

import json

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media
from django.utils.module_loading import import_string
from wagtail.wagtailadmin.rich_text import HalloRichTextArea, DEFAULT_RICH_TEXT_EDITORS


class CustomHalloRichTextArea(HalloRichTextArea):
    @classmethod
    def get_default_options(cls):
        return {
            "plugins": {
                "halloformat": {},
                "halloheadings": {"formatBlocks": ['p', 'h2', 'h3', 'h4', 'h5']},
                "hallolists": {},
                "hallohr": {},
                "halloreundo": {},
                "hallowagtaillink": {},
                "hallorequireparagraphs": {}
            }
        }

    def __init__(self, attrs=None, **kwargs):
        super(CustomHalloRichTextArea, self).__init__(attrs)
        self.kwargs = self.get_default_options()
        if kwargs:
            self.kwargs.update(kwargs)

    def render_js_init(self, id_, name, value):
        return "makeCustomHalloRichTextEditable({0}, {1});".format(json.dumps(id_), json.dumps(self.kwargs))

    @property
    def media(self):
        return Media(js=[
            static('wagtailadmin/js/vendor/hallo.js'),
            static('article/js/custom-hallo-bootstrap.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-wagtaillink.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-hr.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-requireparagraphs.js'),
        ])


def get_rich_text_editor_widget(name='default'):
    editor_settings = getattr(settings, 'WAGTAILADMIN_RICH_TEXT_EDITORS', DEFAULT_RICH_TEXT_EDITORS)

    kwargs = {}
    editor = editor_settings[name]
    options = editor.get('OPTIONS')

    if options:
        kwargs.update(options)

    return import_string(editor['WIDGET'])(**kwargs)
