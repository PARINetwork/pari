from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page


class HomePage(Page):
    URL = "http://localhost:8000"
    home_page_container = (By.CSS_SELECTOR, ".home-page")

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.home_page_container))
        return self
