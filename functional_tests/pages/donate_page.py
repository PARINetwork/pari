from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page

class DonatePage(Page):

    donate_page_container = (By.CSS_SELECTOR, ".donate")

    def __init__(self, driver, relative_url='/'):
        super(DonatePage, self).__init__(driver, self.donate_page_container, '/pages/donate/')
