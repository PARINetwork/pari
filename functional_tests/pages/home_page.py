from selenium.webdriver.common.by import By
from functional_tests.base import Page


class HomePage(Page):
    home_page_container = (By.CSS_SELECTOR, ".home-page")

    def __init__(self, driver, relative_url='/'):
        super(HomePage, self).__init__(driver, self.home_page_container, '/')

    def all_that_you_can_discover_on_pari_section(self):
        return AllThatYouCanDiscoverOnPARISection(self.driver)

    def in_focus_section(self):
        return InFocusSection(self.driver)

    def featured_section(self):
        return FeaturedSection(self.driver)

    def audio_and_video_section(self):
        return ManyMoreStoriesInAudioAndVideoSection(self.driver)


class AllThatYouCanDiscoverOnPARISection():
    def __init__(self, driver):
        self.driver = driver

    def title_of_first_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid large category-0']//h3").text

    def sub_text_of_first_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid large category-0']//div[@class='title-grid resource-description']/div[2]").text

    def title_of_second_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid category-1']//h3").text

    def sub_text_of_second_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid category-1']//div[@class='title-grid']/div[2]").text

    def title_of_third_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid category-2']//div[@class='category-name']/h3").text

    def sub_text_of_third_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid category-2']//div[@class='title-grid']/div[2]").text

    def title_of_fourth_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid category-3']//div[@class='category-name']/h3").text

    def sub_text_of_fourth_category(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='col-lg-6 col-md-6 col-sm-12 col-xs-12 grid category-3']//div[@class='title-grid']/div[2]").text


class InFocusSection():
    def __init__(self, driver):
        self.driver = driver

    def title_of_first_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page1']//div[@class='infocus-item-title']").text

    def authors_of_first_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page1']//div[@class='authors']").text

    def location_of_first_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page1']//span[@class='location-name']").text

    def date_of_first_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page1']//a/span[@class='date link-dark']").text
    
    def title_of_second_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page2']//div[@class='infocus-item-title']").text

    def authors_of_second_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page2']//div[@class='authors']").text

    def location_of_second_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page2']//span[@class='location-name']").text

    def date_of_second_article(self):
        return self.driver.find_element(By.XPATH, "//div[@class='row in_focus_page2']//a/span[@class='date link-dark']").text


class FeaturedSection():
    def __init__(self, driver):
        self.driver = driver

    def featured_label(self):
        return self.driver.find_element(By.XPATH, "//div[@class=' active item content-1']//span[@class='featured']").text

    def title(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class=' active item content-1']//div[@class='featured-content-title']").text

    def link_text(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class=' active item content-1']//div[@class='link-to-page']/a/span").text

    
class ManyMoreStoriesInAudioAndVideoSection():
    def __init__(self, driver):
        self.driver = driver

    def title_of_talking_album(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid talking-album']//h4[@class='item-section-title']").text

    def author_of_talking_album(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid talking-album']//span[@class='author-name']").text

    def title_of_video(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid video']//h4[@class='item-section-title']").text

    def author_of_video(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid video']//span[@class='author-name']").text

    def title_of_photo_album(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid photo-album']//h4[@class='item-section-title']").text

    def author_of_photo_album(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 grid photo-album']//span[@class='author-name']").text
