from __future__ import absolute_import, unicode_literals

import json

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media, widgets
from wagtail.utils.widgets import WidgetWithScript
from wagtail.wagtailadmin.edit_handlers import RichTextFieldPanel
from wagtail.wagtailcore.rich_text import DbWhitelister, expand_db_html


class CustomHalloRichTextArea(WidgetWithScript, widgets.Textarea):
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

    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, attrs=None):
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value, for_editor=True)
        return super(CustomHalloRichTextArea, self).render(name, translated_value, attrs)

    def render_js_init(self, id_, name, value):
        return "makeCustomHalloRichTextEditable({0}, {1});".format(json.dumps(id_), json.dumps(self.kwargs))

    def value_from_datadict(self, data, files, name):
        original_value = super(CustomHalloRichTextArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return DbWhitelister.clean(original_value)

    @property
    def media(self):
        return Media(js=[
            static('wagtailadmin/js/vendor/hallo.js'),
            static('article/js/custom-hallo-bootstrap.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-wagtaillink.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-hr.js'),
            static('wagtailadmin/js/hallo-plugins/hallo-requireparagraphs.js'),
        ])
