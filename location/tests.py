from django.test import TestCase
from django.test import RequestFactory
from .views import LocationDetail
from functional_tests.factory import LocationFactory
from functional_tests.factory import ArticleFactory
from functional_tests.factory import PhotoAlbumSlideFactory
from functional_tests.factory import ImageFactory
import shutil

class LocationDetailTests(TestCase):
    def setUp(self):
        shutil.copy2('core/static/img/stories-1.jpg', 'media/uploads/stories-1.jpg')
        self.location = LocationFactory(name="chennai", id="100")
        self.english_article = ArticleFactory(title="english_article", locations=(self.location,), language='en')
        self.hindi_article = ArticleFactory(title="hindi_article", locations=(self.location,), language='hi')
        image = ImageFactory.create(locations=(self.location,))
        self.english_album = PhotoAlbumSlideFactory(image=image).page

    def test_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/locations/100-chennai/?lang=hi')
        response = LocationDetail.as_view()(request, object=self.location, slug="100-chennai")
        for article in response.context_data['articles']:
            assert article.title == self.hindi_article.title

    def test_lang_is_set_to_english_by_default(self):
        request = RequestFactory().get('/locations/100-chennai/')
        response = LocationDetail.as_view()(request, object=self.location, slug="100-chennai")
        for article in response.context_data['articles']:
            self.assertIn(article.title, [self.english_article.title, self.english_album.title])

    def test_all_articles_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/locations/100-chennai/?lang=all')
        response = LocationDetail.as_view()(request, object=self.location, slug="100-chennai")
        assert len(list((response.context_data['articles']))) == 3
