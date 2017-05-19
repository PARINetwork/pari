from functional_tests.base import Test
from functional_tests.pages import HomePage
from functional_tests.factory import HomePageFactory
from functional_tests.factory import ArticleFactory
from functional_tests.factory import AuthorFactory
from functional_tests.factory import LocationFactory
from functional_tests.factory import CategoryFactory

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
        article1 = ArticleFactory.create(title="article1", authors=(author,), categories=(category1,), locations=(location,))
        article2 = ArticleFactory.create(title="article2", authors=(author,), categories=(category2,), locations=(location,))
        HomePageFactory.create(carousel_0=article1, carousel_1=article2, in_focus_page1=article1, in_focus_page2=article2)

    def test_home_page_title(self):
        home = HomePage(self.driver).open().wait_for_loading()
        assert home.title == "People's Archive of Rural India"

