import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""
To run end-to-end, functional tests using selenium webdriver
"""

BASE_URL = 'localhost:8888'


class BaseTests:
    class BaseFunctionalTest(unittest.TestCase):
        driver = None
        base_url = BASE_URL

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(3)

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()

        def select(self, css_selector):
            try:
                return self.driver.find_elements_by_css_selector(css_selector)
            except NoSuchElementException:
                return []

@unittest.skip
class TestHomepage(BaseTests.BaseFunctionalTest):
    def test_homepage_exists(self):
        self.driver.get(self.base_url + '/')
        self.assertIn(self.driver.title, 'Home')


class TestRegistration(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get(self.base_url + '/register')

    def test_register_exists(self):
        self.assertIn(self.driver.title, 'Registration')

    def test_register_has_fields(self):
        self.assertEqual(
            len(self.select('.field')),
            5
        )  # 4 form fields + csrf token field

    def test_register_has_correct_fields(self):
        fields = [field.find_element_by_tag_name('input').get_attribute('id')
            for field in self.select('.field')]

        self.assertEqual(fields[0], 'csrf_token')
        self.assertEqual(fields[1], 'username')
        self.assertEqual(fields[2], 'email')
        self.assertEqual(fields[3], 'password')
        self.assertEqual(fields[4], 'password2')


if __name__ == '__main__':
    unittest.main()
