import factory
from article.models import Article
from django.utils.text import slugify
from functional_tests.factory import ContentTypeFactory


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    path = factory.Sequence(lambda n: u'0001000{}'.format(n))  # Article sequence starts from 00010020
    depth = 2
    numchild = 0
    title = "Article Page"
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2011-10-24 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, name="article", model="article")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    strap = "Article strap"
    content = "<p> Article Content </p>"
    language = "en"

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_seq_num', 20)
