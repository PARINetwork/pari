from django import template
from wagtail.wagtailcore.rich_text import expand_db_html as expand_db_html_

register = template.Library()


@register.filter
def expand_db_html(source):
    return expand_db_html_(source)
