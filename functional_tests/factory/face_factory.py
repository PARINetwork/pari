import factory
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from face.models import Face
from functional_tests.factory import ImageFactory, LocationFactory


class ContentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentType
        django_get_or_create = ('app_label', 'model')

    app_label = "core"
    model = "homepage"


class FaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Face

    path = factory.Sequence(lambda n: u'0001000100{}'.format(n))  # from wagtailcore_pagerevision
    depth = 3
    numchild = 0
    title = 'Face Page'
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    live = True
    has_unpublished_changes = False
    show_in_menus = False
    search_description = ''
    go_live_at = '1995-02-07 12:00'
    expire_at = '2050-12-31 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="face", model="face")
    locked = False
    latest_revision_created_at = '1995-02-07 12:00'
    first_published_at = '1995-02-07 12:00'

    language = 'en'
    occupation = 'farmer'
    occupation_of_parent = ''
    adivasi = ''
    quote = ''
    child = 'f'
    age = '22'
    gender = 'M'
    image = factory.SubFactory(ImageFactory, title='face image')
    location = factory.SubFactory(LocationFactory)

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_sequence_num', 20)
