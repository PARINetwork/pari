from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page


class AcknowledgementPage(Page):
    home_page_container = (By.CSS_SELECTOR, ".acknowledgements")

    def __init__(self, driver, relative_url='/'):
        super(AcknowledgementPage, self).__init__(driver, '/pages/acknowledgements/')

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.home_page_container))
        return self
