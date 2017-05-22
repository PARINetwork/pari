import unittest
from selenium import webdriver
from author.models import Author
from category.models import Category
from location.models import Location
from core.models import AffixImage, HomePage
from article.models import Article
from album.models import Album

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def load_page_if_not_loaded(self, page, page_lambda):
        if page:
            return page
        else:
            return page_lambda().open().wait_for_loading()

    @classmethod
    def tearDownClass(cls):
        HomePage.objects.all().delete()
        Album.objects.all().delete()
        Article.objects.all().delete()
        AffixImage.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        cls.driver.quit()
