import unittest
from selenium import webdriver
from django.core.management import call_command

class Test(unittest.TestCase):

    def setUp(self):
        call_command('loaddata', 'fixtures/author', verbosity=0)
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
