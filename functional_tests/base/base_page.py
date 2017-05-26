from selenium.webdriver.support.wait import WebDriverWait

class Page(object):

    def __init__(self, driver, element_to_be_loaded, relative_url='/'):
        self.element_to_be_loaded = element_to_be_loaded
        self.base_url = "http://localhost:8000"+relative_url
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    @property
    def url(self):
        return self.driver.current_url

    def wait_for_loading(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(*self.element_to_be_loaded))
        return self

    def open(self):
        self.driver.get(self.base_url)
        return self
