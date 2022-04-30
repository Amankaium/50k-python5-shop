from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class RegisterTest(TestCase):
    def test_rong_pass(self):      
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        driver.find_element_by_link_text('Регистрация').click()

        name = driver.find_element_by_name('firstname')
        name.send_keys('Тестовое имя')

        location = driver.find_element_by_name('lastname')
        location.send_keys('ТестФамилия')

        description = driver.find_element_by_name('username')
        description.send_keys('Псевдоним11')

        description = driver.find_element_by_name('email')
        description.send_keys('email@local.com')

        description = driver.find_element_by_name('password')
        description.send_keys('111')

        description = driver.find_element_by_name('confirm_password')
        description.send_keys('1111')

     
        driver.find_element_by_name('register_button').click()

        sleep(5)

      
        driver.close()

    def test_excist_user(self):      
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        driver.find_element_by_link_text('Регистрация').click()

        name = driver.find_element_by_name('firstname')
        name.send_keys('Тестовое имя')

        location = driver.find_element_by_name('lastname')
        location.send_keys('ТестФамилия')

        description = driver.find_element_by_name('username')
        description.send_keys('Псевдоним')

        description = driver.find_element_by_name('email')
        description.send_keys('email@local.com')

        description = driver.find_element_by_name('password')
        description.send_keys('111')

        description = driver.find_element_by_name('confirm_password')
        description.send_keys('111')

     
        driver.find_element_by_name('register_button').click()

        sleep(5)
        driver.close()


    def test_excist_email(self):      
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000")
        driver.find_element_by_link_text('Регистрация').click()

        name = driver.find_element_by_name('firstname')
        name.send_keys('Тестовое имя')

        location = driver.find_element_by_name('lastname')
        location.send_keys('ТестФамилия')

        description = driver.find_element_by_name('username')
        description.send_keys('Псевдоним1')

        description = driver.find_element_by_name('email')
        description.send_keys('email@local.com')

        description = driver.find_element_by_name('password')
        description.send_keys('111')

        description = driver.find_element_by_name('confirm_password')
        description.send_keys('111')

     
        driver.find_element_by_name('register_button').click()

        sleep(5)
        driver.close()

