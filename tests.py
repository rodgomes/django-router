from django.test import TestCase
from router import Parser

class TestApp(TestCase):

    def test_simple_view(self):
        resp = self.client.get('/simple_view')
        self.assertEqual(200, resp.status_code)

    def test_view_with_param(self):
        resp = self.client.get('/view_with_param/thisIsAParam/')
        self.assertEqual(200, resp.status_code)
        self.assertContains(resp, 'thisIsAParam')

    def test_view_with_default_param(self):
        resp = self.client.get('/view_with_default_param/')
        self.assertEqual(200, resp.status_code)
        self.assertContains(resp, '123')

