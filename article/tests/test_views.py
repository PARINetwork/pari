from django.contrib.auth.models import User
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase

from article.views import AuthorArticleList, ArchiveDetail
from functional_tests.factory import ArticleFactory
from functional_tests.factory import AuthorFactory
from functional_tests.factory import CategoryFactory


def get_title(articles):
    title = ""
    for article in articles:
        title = article.title
    return title


class ArticleDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = AuthorFactory(name='test', slug="test")
        self.article = ArticleFactory(title="test article", authors=(self.author,), language='en')
        self.article = ArticleFactory(title="test modular article", show_modular_content=True)

    def login_admin(self):
        User.objects.create_superuser('pari', 'pari@test.com', "pari")
        self.client.login(username="pari", password="pari")

    def test_curent_page_should_return_article_detail(self):
        response = self.client.get('/articles/test-article/')
        self.assertEqual(response.context_data['current_page'], 'article-details')

    def test_curent_page_should_return_article_template(self):
        response = self.client.get('/articles/test-article/')
        self.assertTemplateUsed(response, 'article/article.html')

    def test_curent_page_should_return_modular_article_paragraph_template(self):
        response = self.client.get('/articles/test-modular-article/')
        self.assertTemplateUsed(response, 'article/blocks/paragraph.html')


class AuthorArticleListTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = CategoryFactory()
        self.test_author1 = AuthorFactory(name='xyz', slug="xyz")
        self.test_author2 = AuthorFactory(name='abc', slug="abc")
        self.english_article = ArticleFactory(title="english_article", authors=(self.test_author1,), language='en',
                                              first_published_at='2011-10-24 12:43')
        self.hindi_article = ArticleFactory(title="hindi_article", authors=(self.test_author1, self.test_author2),
                                            language='hi',
                                            first_published_at='2011-10-25 12:43')
        self.dummy_article = ArticleFactory(title="dummy_article", authors=(self.test_author2,),
                                            language='en',
                                            first_published_at='2011-10-23 12:43')

    def test_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/authors/xyz/?lang=hi')
        response = AuthorArticleList.as_view()(request, slug='xyz')
        title = get_title(response.context_data['articles'])
        assert title == self.hindi_article.title

    def test_lang_is_set_to_english_by_default(self):
        request = RequestFactory().get('/authors/xyz/')
        response = AuthorArticleList.as_view()(request, object=self.category, slug="xyz")
        title = get_title(response.context_data['articles'])
        assert title == self.english_article.title

    def test_all_articles_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/authors/xyz/?lang=all')
        response = AuthorArticleList.as_view()(request, object=self.category, slug="xyz")
        assert len(response.context_data['articles']) == 2

    def test_articles_are_returned_in_desc_order_of_published_date(self):
        response = self.client.get('/authors/xyz/?lang=all')
        self.assertEqual(response.context_data['articles'][0].title, 'hindi_article')

    def test_articles_are_returned_for_the_particular_author(self):
        response = self.client.get('/authors/abc/?lang=all')
        self.assertEqual(response.context_data['articles'][1].title, 'dummy_article')

    def test_articles_are_only_12_in_a_page_for_the_author_xyz(self):
        # Creating 14 articles
        for name in range(1, 15):
            ArticleFactory(title="article" + str(name), authors=(self.test_author1,))
        response_for_page_one = self.client.get('/authors/xyz/?lang=all')
        response_for_page_two = self.client.get('/authors/xyz/?page=2&lang=all')
        self.assertEqual(len(response_for_page_one.context_data['articles']), 12)
        self.assertEqual(len(response_for_page_two.context_data['articles']), 4)


class ArchiveDetailTests(TestCase):
    def setUp(self):
        client = Client()
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.english_article = ArticleFactory(title="english_article", first_published_at='2017-4-24 12:43',
                                              language='en')
        self.hindi_article = ArticleFactory(title="hindi_article", first_published_at='2017-4-25 12:43', language='hi')

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

    def test_title_in_context_should_be_month_and_year(self):
        request = RequestFactory().get('/archive/2017/4/?lang=all')
        response = ArchiveDetail.as_view()(request, year='2017', month='4')
        self.assertEqual(response.context_data['title'], 'April 2017')

    def test_articles_are_returned_in_desc_order_of_published_date(self):
        response = self.client.get('/archive/2017/4/?lang=all')
        self.assertEqual(response.context_data['articles'][0].title, 'hindi_article')

    def test_articles_are_only_12_in_a_page(self):
        # Creating 14 articles
        for name in range(1, 15):
            ArticleFactory(title="article" + str(name), first_published_at='2017-4-25 12:43')
        response_for_page_one = self.client.get('/archive/2017/4/?lang=all')
        response_for_page_two = self.client.get('/archive/2017/4/?page=2&lang=all')
        self.assertEqual(len(response_for_page_one.context_data['articles']), 12)
        self.assertEqual(len(response_for_page_two.context_data['articles']), 4)
