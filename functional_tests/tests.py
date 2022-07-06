import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from seleniumlogin import force_login
import time

MAX_WAIT = 10
DEMO_MODE = 1


class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.browser = webdriver.Chrome(chrome_options=options)


    def tearDown(self):
        self.browser.quit()
        

    def test_can_start_a_list_for_one_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='tester', password='testing321')
        force_login(user, self.browser, self.live_server_url)
        self.browser.get('{}/christmasflix/'.format(self.live_server_url))
        time.sleep(DEMO_MODE)

        self.assertEqual('The Best Christmas Movies', self.browser.title)

        # He is asked to start a new list
        list_inputbox = self.browser.find_element(By.ID, 'id_new_movie')

        list_inputbox.send_keys('Max Mustermann')
        time.sleep(DEMO_MODE)
        list_inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)
        #self.assertEqual('Max Mustermann\'s Christmas Movie List', self.browser.find_element(By.ID, 'list-title').text)

        # Add movie
        movie_inputbox = self.browser.find_element(By.ID, 'id_new_movie')
        movie_inputbox.send_keys('Die Hard')
        time.sleep(DEMO_MODE)
        movie_inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)
        self.assertEqual('Die Hard', self.browser.find_element(By.ID, 'movie-poster').get_attribute("alt"))

        # Select a movie
        movie_button = self.browser.find_element(By.ID, 'movie-button')
        movie_button.click()
        time.sleep(DEMO_MODE)
        self.assertEqual('Die Hard', self.browser.find_element(By.ID, 'movie-poster').get_attribute("alt"))


