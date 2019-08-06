from django.test import TestCase
from functional_tests.factory import ResourceFactory
from django.test import Client


class ResourceListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.resource1 = ResourceFactory(title='Resource1')
        self.resource2 = ResourceFactory(title='Resource2', first_published_at='2017-07-17 12:00')

    def test_current_page_in_context_is_resource_list(self):
        response = self.client.get('/library/')
        self.assertEqual(response.context_data['current_page'], 'resource-list')

    def test_tab_in_context_is_resources(self):
        response = self.client.get('/library/')
        self.assertEqual(response.context_data['tab'], 'resources')

    def test_resources_are_listed_in_desc_order_of_first_published_date(self):
        response = self.client.get('/library/')
        self.assertEqual(response.context_data['resources'][0].title, 'Resource2')

    def test_resources_should_be_paginated_be_fourty_eight_resources(self):
        ResourceFactory.create_batch(48)
        response = self.client.get('/library/')
        self.assertEqual(len(response.context_data['resources']), 48)
        response = self.client.get('/library/?page=2')
        self.assertEqual(len(response.context_data['resources']), 2)


class ResourceDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.resource1 = ResourceFactory(title='Resource1')

    def test_current_page_in_context_is_resource_detail(self):
        response = self.client.get('/library/resource/resource1/')
        self.assertEqual(response.context_data['current_page'], 'resource-detail')

    def test_heading_should_be_yes_when_factoid_is_present(self):
        response = self.client.get('/library/resource/resource1/')
        self.assertEqual(response.context_data['heading'], 'yes')
