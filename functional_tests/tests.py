import time
import sys
import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import rpgs.models

"""
To run end-to-end, functional tests using selenium webdriver
"""


class BaseTests:
    class BaseFunctionalTest(StaticLiveServerTestCase):
        driver = None
        server_url = None
        @classmethod
        def setUpClass(cls):
            super(BaseTests.BaseFunctionalTest, cls).setUpClass()
            cls.server_url = cls.live_server_url
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(3)

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
            super(BaseTests.BaseFunctionalTest, cls).tearDownClass()

        def select(self, css_selector):
            try:
                return self.driver.find_elements_by_css_selector(css_selector)
            except NoSuchElementException:
                return []


class TestHomepage(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get(self.server_url + '/')

    def test_homepage_exists(self):
        self.assertIn(self.driver.title, 'Home')

    def test_login_link(self):
        self.driver.find_element_by_css_selector('a[href*="login"]').click()
        self.assertIn(self.driver.title, 'Login')

    def test_registration_link(self):
        self.driver.find_element_by_css_selector('a[href*="register"]').click()
        self.assertIn(self.driver.title, 'Registration')

    def test_home_link(self):
        self.driver.find_element_by_css_selector('a[href="/"]').click()
        self.assertIn(self.driver.title, 'Home')


class TestRegistration(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get(self.server_url + '/register')

    def tearDown(self):
        for field in self.select('form p input'):
            if field.get_attribute('type') in ['text', 'email', 'password']:
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
        fields = self.select('form p input')
        fields[0].send_keys('some thing')
        fields[1].send_keys('not an email')
        fields[2].send_keys('password')
        fields[3].send_keys('psswrd')
        self.driver.find_element_by_id('submit').click()

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='some thing')

    def test_validation_works_when_correct(self):
        fields = self.select('form p input')
        fields[0].send_keys('test_user')
        fields[1].send_keys('test@user.com')
        fields[2].send_keys('test_pswd')
        fields[3].send_keys('test_pswd')
        self.driver.find_element_by_id('submit').click()

        usr = User.objects.get(username='test_user')
        self.assertEqual(usr.email, 'test@user.com')
        self.assertNotEqual(usr.password, 'test_pswd')


class TestLogin(BaseTests.BaseFunctionalTest):
    def setUp(self):
        self.driver.get("{}{}".format(self.server_url, '/login'))

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
