from django.utils.html import format_html
from django.conf import settings

from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule


@hooks.register('construct_whitelister_element_rules')
def whitelist_blockquote():
    return {
        'blockquote': attribute_rule({'style': True}),
        'p': attribute_rule({'style': True}),
        'iframe': attribute_rule({
            'style': True, 'src': True,
            'width': True, 'height': True
        })
    }

@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script>
        registerHalloPlugin('hallojustify');
        registerHalloPlugin('halloblock', {{ "elements": ["blockquote"] }});
        registerHalloPlugin('hallorequireparagraphs', {{ "blockElements": ['dd', 'div', 'dl', 'figure', 'form', 'ul', 'ol', 'table', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote'] }}); 
        registerHalloPlugin('hallohtml');
        </script>
        <script src="{0}article/js/slug.js"></script>
        """,
        settings.STATIC_URL
    )

@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        """
        <link rel="stylesheet" href="{0}font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="{0}article/css/hallo-icons.css">
        """,
        settings.STATIC_URL
    )
