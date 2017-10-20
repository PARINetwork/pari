from django.test import TestCase, override_settings
from django.test import RequestFactory
from mock import MagicMock
from wagtail.wagtailsearch.backends.elasticsearch import Elasticsearch

from functional_tests.factory import ArticleFactory, AuthorFactory


class ArticleTests(TestCase):
    def setUp(self):
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.article = ArticleFactory(title="english_article", authors=(self.test_author,), language='en')

    def test_article_to_string_should_be_equal_to_the_title(self):
        self.assertEqual(self.article.title, str(self.article))
        self.assertEqual(str(self.article), 'english_article')

    def test_article_get_absolute_url_returns_the_path_to_the_article(self):
        self.assertRegexpMatches(self.article.get_absolute_url(), '/articles/english_article/?$')

    def test_get_context_of_article_should_have_english_article(self):
        request = MagicMock()
        request.get_host.return_value = 'localhost'
        response = self.article.get_context(request)
        assert response['article'].title == 'english_article'

    def test_get_context_return_site_for_what_is_set_by_request(self):
        request = MagicMock()
        request.get_host.return_value = 'localhost'
        response = self.article.get_context(request)
        self.assertEqual(str(response['site']), 'localhost [default]')

    def test_multiple_authors_can_be_added_to_a_article(self):
        author= AuthorFactory(name='Test')
        article = ArticleFactory(title="Multiple Author Article", authors=(self.test_author,author,))
        self.assertEqual(len(article.authors.all()),2)
        self.assertEqual(article.authors.all()[1].name,'Test')


    # @override_settings(
    #     WAGTAILSEARCH_BACKENDS={
    #         'default': {
    #             'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch',
    #             'INDEX': 'pari',
    #             'ATOMIC_REBUILD': True,
    #             'AUTO_UPDATE': True,
    #         },
    #     })
    # def test_related_articles_are_shown_based_on_search_fields_and_boosts(self):
    #     self.article1 = ArticleFactory(title="hindi", authors=(self.test_author,), language='en')
    #     self.article2 = ArticleFactory(title="someother_english", authors=(self.test_author,), language='en')
    #     elastic_search = Elasticsearch()
    #     elastic_search.refresh_index()
    #     print self.article.related_articles()

