
from django.test import TestCase
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get
from time import sleep
from selenium.webdriver.common.by import By




# class HomepageTest(TestCase):
#     def test_homepage_200(self):
#         response = get("http://127.0.0.1:8000/")
#         assert response.status_code == 200
 

class SeleniumTest(TestCase):
    def test_activation(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        driver.find_element_by_link_text('Войти').click()
        
        name = driver.find_element_by_name('username')
        name.send_keys('Тестовая введения имя админа')

        password = driver.find_element_by_name('password')
        password.send_keys('Тестовая введения пароля')

        button= driver.find_element_by_xpath("//*[contains(., 'Войти')]")
        
        button.click()
      
        sleep(5)
        driver.close()
      




