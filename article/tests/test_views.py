from django.test import TestCase
from django.test import RequestFactory
from article.views import AuthorArticleList, ArchiveDetail
from functional_tests.factory import CategoryFactory
from functional_tests.factory import ArticleFactory
from functional_tests.factory import AuthorFactory


def get_title(articles):
    title = ""
    for article in articles:
        title = article.title
    return title


class AuthorArticleListTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.english_article = ArticleFactory(title="english_article", authors=(self.test_author,), language='en')
        self.hindi_article = ArticleFactory(title="hindi_article", authors=(self.test_author,), language='hi')

    def test_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/authors/xyz/?lang=hi')
        response = AuthorArticleList.as_view()(request, slug='xyz')
        title = get_title(response.context_data['articles'])
        assert title == self.hindi_article.title

    def test_lang_is_set_to_english_by_default(self):
        request = RequestFactory().get('/stories/categories/things-we-do/')
        response = AuthorArticleList.as_view()(request, object=self.category, slug="xyz")
        title = get_title(response.context_data['articles'])
        assert title == self.english_article.title

    def test_all_articles_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/stories/categories/things-we-do/?lang=all')
        response = AuthorArticleList.as_view()(request, object=self.category, slug="xyz")
        assert len(response.context_data['articles']) == 2


class ArchiveDetailTests(TestCase):
    def setUp(self):
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.english_article = ArticleFactory(title="english_article", first_published_at='2017-4-24 12:43',
                                              language='en')
        self.hindi_article = ArticleFactory(title="hindi_article", first_published_at='2017-4-24 12:43', language='hi')

    def test_query_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/archive/2017/4/?lang=hi')
        response = ArchiveDetail.as_view()(request, year='2017', month='4')
        title = get_title(response.context_data['articles'])
        assert title == self.hindi_article.title

    def test_lang_is_set_to_english_by_default(self):
        request = RequestFactory().get('/archive/2017/4/')
        response = ArchiveDetail.as_view()(request, year='2017', month='4')
        title = get_title(response.context_data['articles'])
        assert title == self.english_article.title

    def test_all_articles_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/archive/2017/4/?lang=all')
        response = ArchiveDetail.as_view()(request, year='2017', month='4')
        assert len(response.context_data['articles']) == 2
