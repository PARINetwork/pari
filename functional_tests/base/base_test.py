import unittest
from selenium import webdriver
from django.core.management import call_command

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def load_page_if_not_loaded(self, page, page_lambda):
        if page:
            return page
        else:
            return page_lambda().open().wait_for_loading()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
