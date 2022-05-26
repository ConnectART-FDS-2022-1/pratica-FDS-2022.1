from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from core.controller import PostController, UserController
from core.models import Post
from django.contrib.auth.models import User


class TestConnectART(LiveServerTestCase):

  def testRegister(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(self.live_server_url + '/register/')

    username = driver.find_element_by_name("username")
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

    assert "ConnectART | Profile" in driver.title


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

    assert "ConnectART | Profile" in driver.title

    delBtn = driver.find_element_by_id('delAccount')
    delBtn.click()

    assert "ConnectART | Delete account" in driver.title

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    passw_conf = driver.find_element_by_name('confirmPassw')
    submit = driver.find_element_by_name('submitBtn')

    username.send_keys('luis')
    password.send_keys('senhalonga123')
    passw_conf.send_keys('senhalonga123')
    submit.click()

    assert "ConnectART | Login" in driver.title

    driver.close()


  def testPostToFeed(self):
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

    assert "ConnectART | Profile" in driver.title

    driver.get(self.live_server_url + '/createpost/')

    title = driver.find_element_by_name('title')
    body = driver.find_element_by_name('body')
    submit = driver.find_element_by_name('submit')

    title.send_keys('this is a test title')
    body.send_keys('this is a test body')
    submit.click()

    posts = driver.find_element_by_name('posts')

    assert "this is a test title" in posts.text


class PostTests(LiveServerTestCase):

  def testShouldGetPosts(self):
    postObj = PostController()
    posts = postObj.getAllPosts()

    # clean test database, should have no posts
    assert len(posts) == 0


  def testShouldCreatePost(self):
    mock_user = User.objects.create_user('connect')

    postObj = PostController()
    posted = postObj.createPost('title', 'body', mock_user)

    assert posted == True


  def testShouldNotCreatePost(self):
    # improper user object
    mock_user = User()

    postObj = PostController()
    posted = postObj.createPost('title', 'body', mock_user)

    assert posted == False
    