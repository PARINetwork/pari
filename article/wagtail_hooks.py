from django.utils.html import format_html
from django.conf import settings

from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule


@hooks.register('construct_whitelister_element_rules')
def whitelist_blockquote():
    return {
        'blockquote': attribute_rule({'style': True}),
        'p': attribute_rule({'style': True}),
        'h2': attribute_rule({'style': True}),
        'h3': attribute_rule({'style': True}),
        'h4': attribute_rule({'style': True}),
        'h5': attribute_rule({'style': True}),
        'iframe': attribute_rule({
            'style': True, 'src': True,
            'width': True, 'height': True
        }),
        'img': attribute_rule({
            'srcset': True, 'class': True,
            'data-srcset': True, 'alt': True,
            'width': True, 'height': True,
            'sizes': True
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
        <style>
        blockquote {{
	    color: #101010;
	    font-size: 1.6em;
	    border: none;
	    font-style: italic;
	    font-weight: bold;
	    margin: 10px 0;
	    padding: 10px;
	    text-align: center;
	    display: block;
        }}

        blockquote::before {{
            content: open-quote;
        }}
	blockquote::after {{
	    content: close-quote;
        }}
        </style>
        """,
        settings.STATIC_URL
    )
