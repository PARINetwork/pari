from selenium.webdriver.common.by import By

from functional_tests.base import Page


class BannerSection():
    # Add all the components of the banner here
    def __init__(self, driver):
        self.driver = driver

    def title_of_the_article(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id='article-gallery-title']").text


class ModularContent():
    def __init__(self, driver):
        self.driver = driver

    def paragraph_module_text(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="main_content"]/div[2]/div/div[2]/div[1]/div/div/div/div[1]').text
    def columnar_paragraph_module_text(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="main_content"]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/p').text


class ArticlePage(Page):
    article_page_container = (By.CSS_SELECTOR, ".article-detail")

    def __init__(self, driver, relative_url='/'):
        super(ArticlePage, self).__init__(driver, self.article_page_container, relative_url)

    def banner_section(self):
        return BannerSection(self.driver)

    def modular_content(self):
        return ModularContent(self.driver)
