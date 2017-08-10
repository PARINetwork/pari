from django.contrib.auth.models import User
from django.test import TestCase, override_settings, Client
from django.test import RequestFactory
from mock import MagicMock
from wagtail.wagtailsearch.backends.elasticsearch import Elasticsearch
from django.db import DataError, IntegrityError
from django.core.exceptions import ValidationError

from article.models import Article
from functional_tests.factory import ArticleFactory, AuthorFactory


class ArticleAdminFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_author = AuthorFactory(name='xyz', slug="xyz")
        self.article = ArticleFactory(title="english_article", authors=(self.test_author,), language='en')

    def login_admin(self):
        User.objects.create_superuser('pari', 'pari@test.com', "pari")
        self.client.login(username="pari", password="pari")

    def test_no_article_can_be_stored_without_a_title(self):
        with self.assertRaisesRegexp(ValidationError,
                                     "This field cannot be blank"):  # Slug and title fields cannot be null.
            ArticleFactory(title="")

    def test_article_cannot_be_stored_without_content(self):
        with self.assertRaisesRegexp(ValidationError,
                                     "This field cannot be blank"):
            ArticleFactory(title='Test', content='')

    def test_article_cannot_be_stored_without_language(self):
        with self.assertRaisesRegexp(ValidationError,
                                     "This field cannot be blank"):
            ArticleFactory(title='Test', language='')
