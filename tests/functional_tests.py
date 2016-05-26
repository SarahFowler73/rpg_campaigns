import time
import unittest

from selenium import webdriver

"""
To run end-to-end, functional tests using selenium webdriver
"""

BASE_URL = 'localhost:8888'


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = BASE_URL
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_homepage_exists(self):
        self.driver.get(self.base_url + '/')
        self.assertIn(self.driver.title, 'Home')

    def test_register_exitsts(self):
        self.driver.get(self.base_url + '/register')
        self.assertIn(self.driver.title, 'Registration')


if __name__ == '__main__':
    unittest.main()
