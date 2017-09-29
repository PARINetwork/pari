import factory
from core.models import AffixImageRendition
from functional_tests.factory import ImageFactory


class ImageRenditionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AffixImageRendition

    image = factory.SubFactory(ImageFactory)
    width = 800
    height = 1200
    filter_spec = "fill-355"
    focal_point_key = 200
    file = 'uploads/stories-1.jpg'