from django.test import TestCase
from functional_tests.factory import FaceFactory
from django.test import Client


class FaceListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.face = FaceFactory(title='Lokesh')
        self.second_face = FaceFactory(title='SomeNameOfPerson', location__name='Amravati',
                                       location__slug='45-amravati', location__district='amravati')
        self.third_face = FaceFactory(title='SomeName', location__name='Aamravati',
                                      location__slug='45-aamravati', location__district='aamravati')

    def test_sub_heading_in_context_should_be_people_from_every_indian_district(self):
        response = self.client.get('/categories/faces/')
        self.assertEqual(response.context_data['sub_heading'], 'People from every indian district')

    def test_face_should_come_in_order_of_the_district_names(self):
        response = self.client.get('/categories/faces/')
        self.assertEqual(response.context_data['faces'][0].title, 'SomeNameOfPerson')


class FaceDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.first_face = FaceFactory(title='SomeNameOfPerson', location__name='Amravati',
                                      location__slug='45-amravati', location__district='amravati')
        self.second_face = FaceFactory(title='SomeName', location__name='Aamravati',
                                       location__slug='45-aamravati', location__district='aamravati')

    def test_face_should_be_in_order_in_face_district_page(self):
        response = self.client.get('/categories/faces/a/')
        self.assertEqual(response.context_data['faces'][0].title, 'SomeName')

    def test_the_complete_url_to_face_should_give_all_the_details_of_the_face(self):
        response = self.client.get('/categories/faces/a/somename/')
        self.assertEqual(response.context_data['face'].title, 'SomeName')
