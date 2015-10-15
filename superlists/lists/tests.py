from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import home_page


# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found_homepage = resolve('/')
        self.assertEqual(found_homepage.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.strip().startswith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
