from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.db import DataError, IntegrityError

from author.forms import AuthorAdminForm
from author.models import Author
from functional_tests.factory import AuthorFactory


class AuthorModelTests(TestCase):
    def test_author_string_representaion(self):
        assert str(AuthorFactory()) == 'V. Sasikumar'

    def test_author_slug_for_multiple_unique_author_name(self):
        author_name = 'Author Name Author Name Author Name Author Name Author Name'
        author1 = Author(name=author_name)
        author2 = Author(name=author_name + ' ')
        author3 = Author(name=author_name + '. ')
        author1.save()
        author2.save()
        author3.save()

        assert Author.objects.get(name=author_name).slug == 'author-name-author-name-author-name-author-name-au'
        assert Author.objects.get(name=author_name + ' ').slug == 'author-name-author-name-author-name-author-name-a1'
        assert Author.objects.get(name=author_name + '. ').slug == 'author-name-author-name-author-name-author-name-a2'


class AuthorModelsExceptionTest(TestCase):

    def test_should_throw_error_if_author_name_exceeds_hundred_characters(self):
        author_name = 'Full Metal Havok More Sexy N Intelligent Than Spock And All The Superheroes Combined With Frostnova nova';
        author_with_long_name = Author(name=author_name)
        with self.assertRaises(DataError) as context_message:
            author_with_long_name.save()
            the_exception = context_message.exception
            self.assertEqual(the_exception.error_code, 3)

    def test_should_throw_error_if_author_already_exist(self):
        author_one = Author(name='some author')
        author_two = Author(name='some author')
        with self.assertRaises(IntegrityError) as context_message:
            author_one.save()
            author_two.save()
            the_exception = context_message.exception
            self.assertEqual(the_exception.error_code, 3)

    def test_should_throw_error_if_facebook_and_twitter_name__of_author_exceeds_fifty_characters(self):
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

    def test_author_form_should_be_in_valid_if_mandatory_fields_are_empty(self):
        author_form = AuthorAdminForm()
        self.assertEqual(author_form.is_valid(), False)

class AuthorViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_allow_only_authorized_user_to_add_author(self):
        response = self.client.post('/admin/authors/add/', content_type="application/json", data="{'name':'cool'}")
        self.assertEqual(response.status_code, 302)
        self.assertRegexpMatches(response.url, '/admin/login',
                                 msg="Unauthorized users should be redirected to login page")

    def test_should_save_author_for_valid_form_data(self):
        self.login_admin()
        data = 'name=cool'
        response = self.client.post('/admin/authors/add/', data=data,
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        author_from_db = Author.objects.get(slug='cool')
        self.assertEqual(author_from_db.name,'cool')

    def test_should_add_translator_or_photographers_redirect_to_add_author_form(self):
        self.login_admin()
        response_for_add_translator = self.client.get('/admin/translators/add/')
        self.assertEqual(response_for_add_translator.status_code, 302)
        self.assertRegexpMatches(response_for_add_translator.url, "/admin/authors/add/", msg="Add translators should redirect to add author")

        response_for_add_photgraphers = self.client.get('/admin/photographers/add/')
        self.assertEqual(response_for_add_photgraphers.status_code, 302)
        self.assertRegexpMatches(response_for_add_photgraphers.url, "/admin/authors/add/", msg="Add translators should redirect to add author")

    def login_admin(self):
        User.objects.create_superuser('pari', 'pari@test.com', "pari")
        self.client.login(username="pari", password="pari")
