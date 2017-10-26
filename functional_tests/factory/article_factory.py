import factory
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from article.models import Article


# from functional_tests.factory import ContentTypeFactory


class ContentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentType
        django_get_or_create = ('app_label', 'model')

    app_label = "core"
    model = "homepage"


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ('title', 'path')

    path = factory.Sequence(lambda n: u'00010{}'.format(n))  # Article sequence starts from 0001020
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
    expire_at = '2050-12-31 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="article", model="article")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    strap = "Article strap"
    content = "<p> Article Content </p>"

    show_modular_content = False
    modular_content = '[{"type": "paragraph", "id": "b5f88ce7-057f-4c3c-9901-1d675157800c", "value": {"content": "<p>This is a text</p>", "align_content": "default"}}]'

    language = "en"

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_seq_num', 20)

    @factory.post_generation
    def featured_image(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.featured_image = extracted

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for author in extracted:
                self.authors.add(author)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def locations(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for location in extracted:
                self.locations.add(location)
