from django.test import TestCase
from functional_tests.factory import FaceFactory


class Facetest(TestCase):
    def setUp(self):
        self.face = FaceFactory(title='Lokesh')

    def test_title_to_share_returns_meet_Lokesh__farmer_from_sivaganga_tamil_nadu(self):
        self.assertEqual(self.face.title_to_share,'Meet Lokesh, farmer from Sivaganga, Tamil Nadu')

    def test_featured_image_returnes_the_image(self):
        self.assertEqual(self.face.featured_image,self.face.image)

    def test_to_str_returns_lokesh_sivaganga(self):
        self.assertEqual(str(self.face),'Lokesh Sivaganga')

    def test_get_absolute_url_return_path_with_faces_s_face_page(self):
        self.assertEqual(self.face.get_absolute_url(),'/categories/faces/s/lokesh/')