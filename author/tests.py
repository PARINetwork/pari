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


    def test_author_slug_for_multiple_unique_author_name(self):
        author_name = 'Author Name Author Name Author Name Author Name Author Name'
        author1 = Author(name=author_name)
        author2 = Author(name=author_name+' ')
        author3 = Author(name=author_name+'. ')
        author1.save()
        author2.save()
        author3.save()

        assert Author.objects.get(name=author_name).slug == 'author-name-author-name-author-name-author-name-au'
        assert Author.objects.get(name=author_name+' ').slug == 'author-name-author-name-author-name-author-name-a1'
        assert Author.objects.get(name=author_name+'. ').slug == 'author-name-author-name-author-name-author-name-a2'