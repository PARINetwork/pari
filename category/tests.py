from django.test import TestCase
from django.test import RequestFactory
from .views import StoryDetail
from functional_tests.factory import CategoryFactory
from functional_tests.factory import ArticleFactory

def get_title(articles):
    title = ""
    for article in articles:
        title = article.title
    return title

class StoryDetailTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.english_article = ArticleFactory(title="english_article", categories=(self.category,), language='en')
        self.hindi_article = ArticleFactory(title="hindi_article", categories=(self.category,), language='hi')

    def test_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/stories/categories/things-we-do/?lang=hi')
        response = StoryDetail.as_view()(request, object=self.category, slug="things-we-do")
        title = get_title(response.context_data['articles'])
        assert title == self.hindi_article.title

    def test_lang_is_set_to_english_by_default(self):
        request = RequestFactory().get('/stories/categories/things-we-do/')
        response = StoryDetail.as_view()(request, object=self.category, slug="things-we-do")
        title = get_title(response.context_data['articles'])
        assert title == self.english_article.title

    def test_all_articles_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/stories/categories/things-we-do/?lang=all')
        response = StoryDetail.as_view()(request, object=self.category, slug="things-we-do")
        assert len(response.context_data['articles']) == 2
