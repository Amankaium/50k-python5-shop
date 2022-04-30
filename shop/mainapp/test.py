from django.test import TestCase
from requests import get

# Create your tests here.

class HomepageTest(TestCase):
    def test_homepage_200(self):
        response = get("http://127.0.0.1:8000/")
        assert response.status_code == 200