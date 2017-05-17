from functional_tests.base import Test
from functional_tests.pages import DonatePage


class TestDonatePage(Test):
    def test_donate_page_title(self):
        donate_home = DonatePage(self.driver).open().wait_for_loading()
        donate_home_title = self.driver.find_element_by_class_name('donate-title').text.rstrip()

        assert donate_home.title == "Donate to PARI"
        assert donate_home_title == "In 2014-15, only about 0.24% of front page news came out of rural India.\nWe want to change that."
