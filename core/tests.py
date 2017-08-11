from django.core.exceptions import ValidationError
from django.test import RequestFactory
from django.test import TestCase
from wagtail.wagtailimages.models import Filter

from core import models
from core.models import HomePageAdminForm, AffixImage
from core.utils import filter_by_language
from mock import MagicMock

from functional_tests.factory import ImageFactory, AuthorFactory, LocationFactory, CategoryFactory, \
    GalleryHomePageFactory
from functional_tests.factory.image_rendition_factory import ImageRenditionFactory


class FilterByLanguageTests(TestCase):
    def test_lang_is_used_from_query_params(self):
        request = RequestFactory().get('/locations/100-chennai/?lang=hi')
        articles_query_to_filter = MagicMock()
        articles_result_after_filter = ["article1", "article2"]
        articles_query_to_filter.filter.return_value = articles_result_after_filter
        filtered_result = filter_by_language(request, articles_query_to_filter)

        articles_query_to_filter.filter.assert_called_with(language="hi")
        assert filtered_result == (['article1', 'article2'],)

    def test_english_is_chosen_if_no_lang_is_passed_in_query_param(self):
        request = RequestFactory().get('/locations/100-chennai/')
        articles_query_to_filter = MagicMock()
        articles_result_after_filter = ["article1", "article2"]
        articles_query_to_filter.filter.return_value = articles_result_after_filter
        filtered_result = filter_by_language(request, articles_query_to_filter)

        articles_query_to_filter.filter.assert_called_with(language="en")
        assert filtered_result == (['article1', 'article2'],)

    def test_no_filter_is_applied_and_all_given_items_are_returned_if_lang_is_all(self):
        request = RequestFactory().get('/locations/100-chennai/?lang=all')
        articles_query_to_filter = MagicMock()
        articles_result_after_filter = ["article1", "article2"]
        articles_query_to_filter.filter.return_value = articles_result_after_filter
        filtered_result = filter_by_language(request, articles_query_to_filter)

        assert not articles_query_to_filter.filter.called
        assert filtered_result == (articles_query_to_filter,)

    def test_all_items_are_filtered_when_multiple_items_to_be_filtered_is_given(self):
        request = RequestFactory().get('/locations/100-chennai/')
        articles_query_to_filter = MagicMock()
        albums_query_to_filter = MagicMock()
        articles_result_after_filter = ["article1", "article2"]
        albums_result_after_filter = ["album1"]
        articles_query_to_filter.filter.return_value = articles_result_after_filter
        albums_query_to_filter.filter.return_value = albums_result_after_filter
        filtered_result = filter_by_language(request, articles_query_to_filter, albums_query_to_filter)
        
        articles_query_to_filter.filter.assert_called_with(language="en")
        albums_query_to_filter.filter.assert_called_with(language="en")
        assert filtered_result == (articles_result_after_filter, albums_result_after_filter)

class CoreModelTests(TestCase):

    def test_integer_block_should_accept_only_positive_values(self):
        with self.assertRaises(ValidationError) as context_message:
            #arrange
            integer_block = models.IntegerBlock(max_value=100, default=20,)
            #act
            html = integer_block.render_form(100, prefix="integer_field")
            #assert
            self.assertIn('<input id="integer_field" name="integer_field" placeholder="" type="text" value="100" />', html)
            integer_block.clean(-25)

class AffixImageTests(TestCase):

    def setUp(self):
        self.author = AuthorFactory()
        self.author1 = AuthorFactory(name="donald", slug="donald")
        self.location = LocationFactory()
        self.category=CategoryFactory()
        self.image = ImageFactory(photographers=(self.author,self.author1), locations=(self.location,), categories=(self.category,))

    def test_should_return_all_photographers_of_image(self):
        photographers = self.image.get_all_photographers()
        print photographers
        self.assertEqual('V. Sasikumar donald',photographers)

    def test_should_return_all_locations(self):
        locations = self.image.get_locations_index()
        self.assertEqual('Sivaganga  Sivaganga  Tamil Nadu',locations)

    def test_alt_text(self):
        alt_text = self.image.alt_text
        self.assertEqual('PARI Stories from all over in all languages',alt_text)

    def test_default_alt_text(self):
        default_alt_text = self.image.default_alt_text
        print default_alt_text
        self.assertEqual('PARI Stories from all over in all languages',default_alt_text)

    def test_categories_index(self):
        categories_index = self.image.get_categories_index()
        self.assertEqual(1, len(categories_index))
        self.assertEqual(self.category.id, (categories_index)[0])

    def test_image_str(self):
        title = self.image.__str__()
        self.assertEqual('loom',title)

class AffixImageRenditionTests(TestCase):

    def setUp(self):
        filter = Filter(spec="fill-355")
        filter.save()
        self.image_rendition = ImageRenditionFactory(filter_id=filter.id)

    def test_img_tag(self):
        image_rendition_tag = self.image_rendition.img_tag()
        self.assertEqual('<img alt="loom" height="1200" src="/media/uploads/stories-1.jpg" width="800">', image_rendition_tag)














