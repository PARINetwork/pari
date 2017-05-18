from functional_tests.base import Test
from functional_tests.pages import HomePage
from functional_tests.factory import HomePageFactory

class TestHomePage(Test):
    @classmethod
    def setUpClass(cls):
        super(TestHomePage, cls).setUpClass()
        page = HomePageFactory.create()
        # page2 = PageFactory.create()

    def test_home_page_title(self):
        home = HomePage(self.driver).open().wait_for_loading()
        assert home.title == "People's Archive of Rural India"

