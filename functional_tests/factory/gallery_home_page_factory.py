import factory
from core.models import GalleryHomePage
from functional_tests.factory import ContentTypeFactory
from functional_tests.factory.article_factory import ArticleFactory
from functional_tests.factory.album_factory import AlbumFactory
from functional_tests.factory.image_factory import ImageFactory

class GalleryHomePageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GalleryHomePage

    path = "0001000A"
    depth = 2
    numchild = 0
    slug = "gallery"
    title = "Gallery Home Page"
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2011-10-24 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="core", model="galleryhomepage")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    photo_of_the_week = factory.SubFactory(ImageFactory)
    photo_title = "Gallery title"
    photo_link = "http://www.google.com"
    talking_album = factory.SubFactory(AlbumFactory)
    photo_album = factory.SubFactory(AlbumFactory)
    video = factory.SubFactory(ArticleFactory, title="carousel_0", content_type__app_label="article", content_type__model="article")
