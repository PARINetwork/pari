from django.test import TestCase
from functional_tests.factory import ResourceFactory


class ResourceTests(TestCase):
    def setUp(self):
        self.resource = ResourceFactory()

    def test_to_string_should_be_equal_to_the_title(self):
        self.assertEqual(self.resource.title, str(self.resource))

    def test_absolute_url_points_to_dummy_resource_page(self):
        self.assertEqual(self.resource.get_absolute_url(),'/library/resource/dummy-resource-page/')
