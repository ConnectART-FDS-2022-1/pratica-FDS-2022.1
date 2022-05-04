from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestConnectART(LiveServerTestCase):

  def testRegister(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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

  def testLogin(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    submit = driver.find_element_by_name('submitBtn')

    username.send_keys('luis')
    password.send_keys('senhalonga123')
    submit.click()

    assert "ConnectART | Perfil" in driver.title

  def testDelAccount(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    submit = driver.find_element_by_name('submitBtn')

    username.send_keys('luis')
    password.send_keys('senhalonga123')
    submit.click()

    assert "ConnectART | Perfil" in driver.title

    delBtn = driver.find_element_by_id('delAccount')
    delBtn.click()

    assert "ConnectART | Login" in driver.title

    driver.close()
