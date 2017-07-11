<<<<<<< 27017939cae8d8ad89e4f36d3d64cdfce074355a
from django.test import TestCase, RequestFactory
from mock import MagicMock

from functional_tests.factory import ArticleFactory, CategoryFactory, AuthorFactory


class AlbumTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.article = ArticleFactory(title='english_article', authors=(self.test_author,), language='en')

    def test_absolute_url_should_give_the_absolute_path_with_slug(self):
        assert self.article.get_absolute_url() == '/articles/english_article/'

    def test_get_context_of_article_should_have_english_article(self):
        request = MagicMock()
        response = self.article.get_context(request)
        assert response['article'].title == 'english_article'

    def test_get_context_return_site_for_what_is_set_by_request(self):
        request = MagicMock()
        response = self.article.get_context(request)
        response.get_host.return_value = 'localhost'
        print response['site']
=======
from django.test import TestCase
from django.test import RequestFactory

from functional_tests.factory import ArticleFactory, AuthorFactory


class ArticleTests(TestCase):
    def setUp(self):
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.article = ArticleFactory(title="english_article", authors=(self.test_author,), language='en')

    def test_article_to_string_should_be_equal_to_the_title(self):
        self.assertEqual(self.article.title, str(self.article))
        self.assertEqual(str(self.article), 'english_article')

    def test_article_get_absolute_url_returns_the_path_to_the_article(self):
        self.assertEqual(self.article.get_absolute_url(), '/articles/english_article/')
>>>>>>> Added basic model test for article
