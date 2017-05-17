from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page


class DonatePage(Page):

    donate_page_container = (By.CSS_SELECTOR, ".donate")

    def __init__(self, driver, relative_url='/'):
        super(DonatePage, self).__init__(driver, '/pages/donate/')

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.donate_page_container))
        return self