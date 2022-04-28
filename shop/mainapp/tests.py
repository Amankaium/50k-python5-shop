from urllib import response
from django.test import TestCase
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get



class HomepageTest(TestCase):
    def test_homepage_200(self):
        response = get("http://127.0.0.1:8000/")
        assert response.status_code == 200



class loginTest(TestCase):
    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200) 


class seleniumTest(TestCase):
    def test_authorization(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

     


