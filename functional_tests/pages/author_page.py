from selenium.webdriver.common.by import By

from functional_tests.base import Page

class AuthorPage(Page):
    author_page_container = (By.CSS_SELECTOR, ".author-detail")

    def __init__(self, driver, relative_url='/'):
        super(AuthorPage, self).__init__(driver, self.author_page_container, relative_url)

    def author_name(self):
        return self.driver.find_element_by_css_selector(".author-name").text
