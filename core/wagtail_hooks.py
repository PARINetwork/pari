from django.conf import settings
from django.utils.html import format_html
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script src="{0}article/js/slug.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                $('h1:contains("Editing Static page Acknowledgements"),h1:contains("Editing Static page About PARI"),h1:contains("Editing Static page PARI Students & Teachers"), h1:contains("Editing Static page Founder Editor P Sainath"),h1:contains("Editing Static page Contribute"),h1:contains("Editing Static page Donate to Pari"),h1:contains("Editing Static page Donate")').parents('header').siblings('form').find('h2:contains("Content")').children('label').text('CONTENT is not used anywhere. Purpose of having text here is only for elastic search indexing')
                $('h2:contains("CONTENT is not used anywhere") ~ fieldset .hallo_rich_text_area .richtext').attr('contenteditable', false);
            }});
        </script>
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
        .center {{ text-align: center; }}
        .left {{ text-align: left; }}
        .right {{ text-align: right; }}
        .justify {{ text-align: justify; }}
        </style>
        """,
        settings.STATIC_URL
    )
