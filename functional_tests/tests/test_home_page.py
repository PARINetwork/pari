from functional_tests.base import Test
from functional_tests.pages import HomePage


class TestHomePage(Test):

    def test_home_page_title(self):
        home = HomePage(self.driver).open().wait_for_loading()
        assert home.title == "Peoples Archive of rural india"

