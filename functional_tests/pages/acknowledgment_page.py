from selenium.webdriver.common.by import By
from functional_tests.base import Page

class AcknowledgementPage(Page):
    ack_page_container = (By.CSS_SELECTOR, ".acknowledgements")

    def __init__(self, driver, relative_url='/'):
        super(AcknowledgementPage, self).__init__(driver, self.ack_page_container, '/pages/acknowledgements/')
