import factory
from core.models import AffixImage

class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AffixImage

    title = "loom"
    file = "uploads/stories-1.jpg"
    width = 3216
    height = 2136
    created_at = "2015-07-31 10:25"
    collection_id = 1
    event = "PARI Stories from all over in all languages"

    @factory.post_generation
    def locations(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for location in extracted:
                self.locations.add(location)

    @factory.post_generation
    def photographers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for photographer in extracted:
                self.photographers.add(photographer)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)