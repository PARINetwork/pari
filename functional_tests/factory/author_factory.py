import factory
from author.models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
        django_get_or_create = ('name', 'email')

    name = "V. Sasikumar"
    slug = "sasikumar-vasudevan"
    email = "sasikumar-vasudevan@gmail.com"
    twitter_username = "@sasi"
    facebook_username = "sasi"
    website = "www.sasi.com"
    bio = "Bio of Sasi"
