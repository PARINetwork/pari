from django.test import TestCase, RequestFactory
from django.db import DataError, IntegrityError

from author.forms import AuthorAdminForm
from author.models import Author
from functional_tests.factory import AuthorFactory
from author.views import add_author, add_photographer, add_translator


class AuthorTests(TestCase):
    def test_string_representaion(self):
        assert str(AuthorFactory()) == 'V. Sasikumar'

    def test_author_slug_for_multiple_unique_author_name(self):
        author_name = 'Author Name Author Name Author Name Author Name Author Name'
        AuthorFactory(name=author_name)
        AuthorFactory(name=author_name + ' ')
        AuthorFactory(name=author_name + '. ')

        self.assertEqual(Author.objects.get(name=author_name).slug,
                         'author-name-author-name-author-name-author-name-au')
        self.assertEqual(Author.objects.get(name=author_name + ' ').slug,
                         'author-name-author-name-author-name-author-name-a1')
        self.assertEqual(Author.objects.get(name=author_name + '. ').slug,
                         'author-name-author-name-author-name-author-name-a2')


class AuthorModelsExceptionTest(TestCase):
    def test_should_throw_error_if_author_name_exceeds_100_characters(self):
        author_name = 'Full Metal Havok More Sexy N Intelligent Than Spock And All The Superheroes Combined With Frostnova nova';
        author_with_long_name = Author(name=author_name)
        with self.assertRaises(DataError) as context_message:
            author_with_long_name.save()
            the_exception = context_message.exception
            self.assertEqual(the_exception.error_code, 3)

    def test_should_throw_error_if_author_names_with_same_name(self):
        author_one = Author(name='some author')
        author_two = Author(name='some author')
        with self.assertRaises(IntegrityError) as context_message:
            author_one.save()
            author_two.save()
            the_exception = context_message.exception
            self.assertEqual(the_exception.error_code, 3)

    def test_should_throw_error_if_facebook_and_twitter_name__of_author_exceeds_50_characters(self):
        with self.assertRaises(DataError) as context_message:
            AuthorFactory(name='some author',
                          twitter_username='JAMIEREDGATE:OggtheCleverFullMetalHavokMoreKnowledgeNIntelligentThanSpockAndAll')
            AuthorFactory(name='some good author',
                          facebook_username='JAMIEREDGATE:OggtheCleverFullMetalHavokMoreKnowledgeNIntelligentThanSpockAndAll')
            the_exception = context_message.exception
            self.assertEqual(the_exception.error_code, 3)


class AuthorAdminFormTest(TestCase):
    def test_author_form_should_not_have_fields_image_and_slug(self):
        author_form = AuthorAdminForm()
        self.assertEqual('image' in author_form.fields, False, msg="AuthorAdminForm should not contain field image")
        self.assertEqual('slug' in author_form.fields, False, msg="AuthorAdminForm should not contain field slug")

    def test_author_form_is_not_valid_if_mandatory_fields_are_empty(self):
        author_form = AuthorAdminForm()
        self.assertEqual(author_form.is_valid(), False)


class AuthorViewsTest(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_add_author_should_return_status_code_200(self):
        request = self.request_factory.get('/admin/authors/add/')
        response = add_author(request)
        self.assertEqual(response.status_code, 200)

    def test_add_translator_or_photographers_should_redirect_to_add_author_form(self):
        request = self.request_factory.get('/admin/translators/add')
        response = add_translator(request)
        self.assertEqual(response.url, "/admin/authors/add/")
        request = self.request_factory.get('/admin/photographers/add')
        response = add_photographer(request)
        self.assertEqual(response.url, "/admin/authors/add/")
