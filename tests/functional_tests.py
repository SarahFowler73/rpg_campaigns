import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""
To run end-to-end, functional tests using selenium webdriver
"""

BASE_URL = 'localhost:8000'


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


class TestHomepage(BaseTests.BaseFunctionalTest):
    def test_homepage_exists(self):
        self.driver.get(self.base_url + '/')
        self.assertIn(self.driver.title, 'Home')


class TestRegistration(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get(self.base_url + '/register')

    def tearDown(self):
        for field in self.select('form p input'):
            if field.get_attribute('type') in ['text', 'password']:
                field.clear()

    def test_register_exists(self):
        self.assertIn(self.driver.title, 'Registration')

    def test_register_has_fields(self):
        self.assertEqual(len(self.select('form p input')), 5)

    def test_register_has_correct_fields(self):
        fields = self.select('form p input')

        self.assertEqual(fields[0].get_attribute('id'), 'id_username')
        self.assertEqual(fields[1].get_attribute('id'), 'id_email')
        self.assertEqual(fields[2].get_attribute('id'), 'id_password')
        self.assertEqual(fields[3].get_attribute('id'), 'id_password2')
        self.assertEqual(fields[4].get_attribute('id'), 'id_pooh')

        self.assertEqual(fields[0].get_attribute('type'), 'text')
        self.assertEqual(fields[1].get_attribute('type'), 'email')
        self.assertEqual(fields[2].get_attribute('type'), 'password')
        self.assertEqual(fields[3].get_attribute('type'), 'password')
        self.assertEqual(fields[4].get_attribute('type'), 'hidden')

    def test_validation_fails_when_incorrect(self):
        pass

    def test_validation_works_when_correct(self):
        pass


class TestLogin(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get(self.base_url + '/login')

    def tearDown(self):
        for field in self.select('form p input'):
            if field.get_attribute('type') in ['text', 'password']:
                field.clear()

    def test_login_exists(self):
        self.assertIn(self.driver.title, 'Login')

    def test_login_has_fields(self):
        self.assertEqual(len(self.select('form p')), 2)

    def test_login_has_correct_fields(self):
        fields = [field.find_element_by_tag_name('input')
            for field in self.select('form p')]

        self.assertEqual(fields[0].get_attribute('id'), 'id_username')
        self.assertEqual(fields[1].get_attribute('id'), 'id_password')

        self.assertEqual(fields[0].get_attribute('type'), 'text')
        self.assertEqual(fields[1].get_attribute('type'), 'password')


if __name__ == '__main__':
    unittest.main()
