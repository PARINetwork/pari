from functional_tests.base import Test
from functional_tests.pages import HomePage
from functional_tests.factory import HomePageFactory
from functional_tests.factory import AuthorFactory
from functional_tests.factory import LocationFactory
from functional_tests.factory import CategoryFactory
from functional_tests.factory import ImageFactory
from functional_tests.data_setup import DataSetup

class TestHomePage(Test):
    @classmethod
    def setUpClass(cls):
        super(TestHomePage, cls).setUpClass()
        author = AuthorFactory.create()
        category1 = CategoryFactory.create(name="Resource Conflicts", slug="resource-conflicts", order=1)
        category2 = CategoryFactory.create(name="Adivasis", slug="adivasis", order=2)
        category3 = CategoryFactory.create(name="Dalits", slug="dalits", order=3)
        category4 = CategoryFactory.create(name="Sports Games", slug="sports-games", order=4)
        location = LocationFactory.create()
        image = ImageFactory.create(photographers=(author,), locations=(location,))
        setup = DataSetup()
        article1 = setup.create_article("article1", author, category1, location, image)
        article2 = setup.create_article("article2", author, category2, location, image)
        video_article = setup.create_video_article("video article", author, location, image)
        talking_album = setup.create_talking_album(image)
        photo_album = setup.create_photo_album(image)
        HomePageFactory.create(carousel_0=article1, carousel_1=article2, in_focus_page1=article1, in_focus_page2=article2, video=video_article, talking_album=talking_album, photo_album=photo_album)

    def test_home_page_title(self):
        home = HomePage(self.driver).open().wait_for_loading()
        assert home.title == "People's Archive of Rural India"

