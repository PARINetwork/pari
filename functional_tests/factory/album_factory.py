import factory
from album.models import Album, AlbumSlide
from django.utils.text import slugify
from functional_tests.factory import ContentTypeFactory

class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    path = factory.Sequence(lambda n: u'000100{}'.format(n))  # Album sequence starts from 00010050
    depth = 2
    numchild = 0
    title = "Album Page"
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2011-10-24 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="album", model="album")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    description = "<p> Album Content </p>"
    language = "en"

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_seq_num', 50)

class TalkingAlbumSlideFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AlbumSlide

    page = factory.SubFactory(AlbumFactory, title='talking album')
    audio = "109687682"
    description = "<p><i>Varavattoor village, Desamangalam panchayat, Wadakkanchery, Kerala</i></p>"
    created_on = "2015-07-31 10:29:49"
    modified_on = "2015-08-31 10:29:49"

    @factory.post_generation
    def image(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.image = extracted

class PhotoAlbumSlideFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AlbumSlide

    page = factory.SubFactory(AlbumFactory, title="photo album")
    description = "<p><i>Kerala's 'Green Army' is addressing low paddy productivity and a shortage of farm labour</i></p>"
    created_on = "2015-07-31 10:29:49"
    modified_on = "2015-08-31 10:29:49"

    @factory.post_generation
    def image(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.image = extracted
