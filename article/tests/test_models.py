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