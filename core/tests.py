from django.test import RequestFactory
from django.test import TestCase
from core.utils import filter_by_language
from mock import MagicMock

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
