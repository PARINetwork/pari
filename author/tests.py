from django.test import TestCase

import factory

from author.models import Author


class AuthorFactory(factory.Factory):
    class Meta:
        model = Author

    name = 'An author'


class AuthorTests(TestCase):
    def test_string_representaion(self):
        assert str(AuthorFactory()) == 'An author'
