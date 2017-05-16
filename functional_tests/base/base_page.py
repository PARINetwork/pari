class Page(object):

    def __init__(self, driver, relative_url='/'):
        self.base_url = "http://localhost:8000"+relative_url
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    @property
    def url(self):
        return self.driver.current_url

    def open(self):
        self.driver.get(self.base_url)
        return self
