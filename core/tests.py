from socket import if_indextoname
from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestConnectART(LiveServerTestCase):

  def testlogin(self):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(self.live_server_url + '/register/')

    username = driver.find_element_by_name('username')
    email = driver.find_element_by_name('email')
    password = driver.find_element_by_name('password')
    passw_conf = driver.find_element_by_name('confirmPassw')
    submit = driver.find_element_by_name('submitBtn')

    username.send_keys('luis')
    email.send_keys('luiscruz@gmail.br')
    password.send_keys('senhalonga123')
    passw_conf.send_keys('senhalonga123')
    submit.click()

    assert "ConnectART | Login" in driver.title

    driver.close()
