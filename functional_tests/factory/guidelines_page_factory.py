import factory
from core.models import GuidelinesPage
from functional_tests.factory import ContentTypeFactory
from wagtail.wagtailcore.rich_text import RichText


class GuidelinesPageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GuidelinesPage

    path = "00010007000B"
    depth = 3
    numchild = 0
    title = "Guidelines Page"
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2011-10-24 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="core", model="guidelinespage")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    strap = "Writers, photographers, filmmakers and others"
    content = [('heading_title', 'Types of Articles and Other Content'), (
        'heading_content', RichText('<p> Many different kinds of articles/writing go up on PARI. There are: </p>')),
               ('sub_section_with_heading', {'heading': 'Full-length feature',
                                             'content': RichText(
                                                 '<p> Ideally, these articles will be 1,000 words or less, on average.</p>')})]
