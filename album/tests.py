from django.test import TestCase, RequestFactory

from album.models import Album
from album.views import AlbumList
from functional_tests.factory import TalkingAlbumSlideFactory, ImageFactory, AuthorFactory, LocationFactory, \
    AlbumFactory, PhotoAlbumSlideFactory


class TalkingAlbumSlideTest(TestCase):
    def setUp(self):
        self.author1 = AuthorFactory.create(name='Test1')
        self.author2 = AuthorFactory.create(name='Test2')
        self.author3 = AuthorFactory.create(name='Test3')
        location1 = LocationFactory.create(name="Madurai", slug="madurai")
        image1 = ImageFactory.create(photographers=(self.author1, self.author2,), locations=(location1,))
        image2 = ImageFactory.create(photographers=(self.author1, self.author3,), locations=(location1,))
        self.album = AlbumFactory(title="Base Album")
        self.talking_album = TalkingAlbumSlideFactory(image=image1, page=self.album)
        self.talking_album1 = TalkingAlbumSlideFactory(image=image2, page=self.album)

    def test_title_of_the_talking_album_should_be_equal_to_the_toStr(self):
        assert self.talking_album.page.title == str(self.talking_album.page)

    def test_album_photographers_returns_unique_photographers(self):
        photographers = self.album.photographers
        assert len(photographers) == 3
        names_of_photographers = map(lambda photographer: photographer.name, photographers)
        self.assertTrue(self.author1.name in names_of_photographers)
        self.assertTrue(self.author2.name in names_of_photographers)
        self.assertTrue(self.author3.name in names_of_photographers)


class AlbumListTest(TestCase):
    def setUp(self):
        author1 = AuthorFactory.create(name='Test1')
        author2 = AuthorFactory.create(name='Test2')
        author3 = AuthorFactory.create(name='Test3')
        location1 = LocationFactory.create(name="Madurai", slug="madurai")
        image1 = ImageFactory.create(photographers=(author1, author2,), locations=(location1,))
        self.talking_album1 = TalkingAlbumSlideFactory(image=image1, page__title="Talking Album 1",
                                                       page__first_published_at='2011-10-24 12:43')
        self.talking_album2 = TalkingAlbumSlideFactory(image=image1, page__title="Talking Album 2",
                                                       page__first_published_at='2011-10-25 12:43')
        self.photo_album = PhotoAlbumSlideFactory(image=image1)

    def request_for_albums(self, album_type):
        request = RequestFactory().get('/albums/' + album_type + '/')
        responseSet = AlbumList.as_view()(request, filter=album_type)
        return responseSet

    def test_request_for_talking_url_should_get_talking_album_in_context(self):
        response = self.request_for_albums('talking')
        title = response.context_data['title']
        assert title == 'Talking Albums'

    def test_count_of_talking_albums_created_should_be_two(self):
        responseSet = self.request_for_albums('talking')
        assert len(responseSet.context_data['albums']) == 2

    def test_count_of_photo_albums_created_should_be_two(self):
        response = self.request_for_albums('other')
        assert len(response.context_data['albums']) == 1

    def test_talking_albums_should_come_in_order_of_first_published_date(self):
        response = self.request_for_albums('talking')
        assert response.context_data['albums'][0].title == 'Talking Album 2'

    def test_should_return_count_two_photographer_for_talking_album_2(self):
        response = self.request_for_albums('talking')
        id_of_talking_album1 = self.talking_album1.id
        self.assertEqual( len(response.context_data['photographers']), 2)
