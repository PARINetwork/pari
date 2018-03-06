import factory
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from wagtail.wagtailcore.rich_text import RichText

from resources.models import Resource


class ContentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentType
        django_get_or_create = ('app_label', 'model')

    app_label = "core"
    model = "homepage"


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource

    path = factory.Sequence(lambda n: u'00010{}'.format(n))  # from wagtailcore_pagerevision
    depth = 3
    numchild = 0
    title = 'Dummy Resource Page'
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    live = True
    has_unpublished_changes = False
    show_in_menus = False
    search_description = ''
    go_live_at = '1995-02-07 12:00'
    expire_at = '2050-12-31 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="resource", model="resource")
    locked = False
    latest_revision_created_at = '1995-02-07 12:00'
    first_published_at = '1995-02-07 12:00'
    language = 'en'

    content = [('authors', RichText('<p>XYZ</p>')),
               ('copyright', RichText('<p>XYZ, Professor, Centre for Economic Studies and Planning</p><p>\u00a0</p>')),
               ('focus',
                RichText('<p>The 2008 global food price fluctuations -- especially the policies on bio-fuel and the neglect of agriculture.</p>')),
               ('factoids', RichText('<p>Lack of public investment in agriculture and agriculture research .</p>'))]

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_sequence_num', 20)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
