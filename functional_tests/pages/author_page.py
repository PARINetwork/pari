from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import Page

class AuthorPage(Page):
    author_page_container = (By.CSS_SELECTOR, ".author-detail")

    def __init__(self, driver, relative_url='/'):
        super(AuthorPage, self).__init__(driver, relative_url)

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.author_page_container))
        return self

    def author_name(self):
        return self.driver.find_element_by_css_selector(".author-name").text
