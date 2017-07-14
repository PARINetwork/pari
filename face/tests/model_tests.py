from django.test import TestCase
from functional_tests.factory import FaceFactory, ImageFactory, LocationFactory, AuthorFactory


class Facetest(TestCase):
    def setUp(self):
        self.face = FaceFactory(title='Lokesh')

    def test_title_to_share_returns_meet_Lokesh__farmer_from_sivaganga_tamil_nadu(self):
        self.assertEqual(self.face.title_to_share,'Meet Lokesh, farmer from Sivaganga, Tamil Nadu')

    