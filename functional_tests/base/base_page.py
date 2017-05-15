class Page(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    @property
    def url(self):
        return self.driver.current_url

    def open(self):
        self.driver.get(self.URL)
        return self
