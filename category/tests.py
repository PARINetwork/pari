from django.db import DataError, IntegrityError
from django.test import TestCase, Client
from django.test import RequestFactory

from category.models import Category
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
        self.english_article = ArticleFactory(title="english_article", categories=(self.category,), language='en', first_published_at='2017-07-06 00:00')
        self.hindi_article = ArticleFactory(title="hindi_article", categories=(self.category,), language='hi', first_published_at='2017-07-08 00:01')
        self.client = Client()

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

    def test_should_story_list_be_ordered_by_first_published_date(self):
        request = RequestFactory().get('/stories/categories/things-we-do/?lang=all')
        response = StoryDetail.as_view()(request, object=self.category, slug="things-we-do")
        self.assertEqual('hindi_article',response.context_data['articles'][0].title)

    def test_context_fields(self):
        request = RequestFactory().get('/stories/categories/things-we-do/?lang=all')
        response = StoryDetail.as_view()(request,object=self.category,slug="things-we-do")
        self.assertEqual(str(response.context_data['title']),'Things we do')
        self.assertEqual(str(response.context_data['sub_heading']),'The world of rural labour')
        self.assertEqual(str(response.context_data['tab']),'stories')
        self.assertEqual(str(response.context_data['current_page']),'single-category')
        self.assertEqual(str(response.context_data['category']),'Things we do')


class CategoryModelTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.my_category = Category(name="my_category")

    def test_should_throw_error_if_category_already_exists(self):
        with self.assertRaises(IntegrityError) as context_message:
            self.my_category.save()
            my_category_1 = Category(name="my_category")
            my_category_1.save()

    def test_should_throw_error_if_name_exceeds_100_character(self):
        with self.assertRaises(DataError) as context_message:
            CategoryFactory(name='Full Metal Havok More Sexy N Intelligent Than Spock And All The Superheroes Combined With Frostnova nova')

    def test_should_throw_error_if_category_order_is_a_negative_value(self):
        with self.assertRaises(IntegrityError) as context_message:
            self.my_category.order = -1
            self.my_category.save()

    def test_absolute_url(self):
        absolute_url = self.category.get_absolute_url()
        self.assertRegexpMatches(absolute_url,'things-we-do')

    def test_str(self):
        self.assertEqual(self.category.__str__(),'Things we do')


