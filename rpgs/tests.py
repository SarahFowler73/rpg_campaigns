from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTest(TestCase):
    def test_index_view(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, 'Home')

    def test_register_view(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('password', resp.context['form'].fields)
        self.assertTemplateUsed(resp, 'register.html')
        self.assertContains(resp, 'Register')

    def test_login_view(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('password', resp.context['form'].fields)
        self.assertTemplateUsed(resp, 'login.html')
        self.assertContains(resp, 'Log In')
