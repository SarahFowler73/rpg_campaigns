from django.http import HttpRequest
from django.contrib.auth.models import User

from django.test import TestCase
from django.core.urlresolvers import reverse

from . import views


class IndexViewTest(TestCase):
    def test_view_displays(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, 'Home')


class RegisterViewTest(TestCase):
    def test_view_displays(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('password', resp.context['form'].fields)
        self.assertTemplateUsed(resp, 'register.html')
        self.assertContains(resp, 'Register')

    def test_redirects_after_post(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'sarah',
                'email': 'sarah@example.com',
                'password': 'password1',
                'password2': 'password1'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_makes_new_user(self):
        self.assertEqual(0, len(User.objects.filter(username='jack')))
        response = self.client.post(
            reverse('register'),
            {
                'username': 'jack',
                'email': 'jack@example.com',
                'password': 'password1',
                'password2': 'password1'
            }
        )
        user = User.objects.get(username='jack')
        self.assertEqual(user.email, 'jack@example.com')


class LoginViewTest(TestCase):
    def test_view_displays(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('password', resp.context['form'].fields)
        self.assertTemplateUsed(resp, 'login.html')
        self.assertContains(resp, 'Log In')

    def test_redirects_after_successful_login(self):
        user = {'username': 'jim', 'password': 'passwd1'}
        User.objects.create_user(email='jim@example.com', **user)

        response = self.client.post(
            reverse('login'),
            user
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_does_not_redirect_on_unsuccessful_login(self):
        fake_user = {'username': 'fake', 'password': 'fake_pwd'}
        response = self.client.post(
            reverse('login'),
            fake_user
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')


class LogoutViewTest(TestCase):
    pass
