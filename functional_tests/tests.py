import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10
DEMO_MODE = 5


# fixme not working in github actions only locally

""" class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        #options = webdriver.FirefoxOptions()
        #options.add_argument("--headless")
        #self.browser = webdriver.Firefox(options=options)
        
        #self.client.login(username='tester', password='testing321')
        self.user = User.objects.create_superuser(username='tester', password='testing321')
        self.client.force_login(self.user)
        self.browser = webdriver.Firefox()
        time.sleep(DEMO_MODE)
        self.browser.get(self.live_server_url)
        


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_for_one_user(self):
        self.client.get('christmasflix/')

        self.assertEqual('The Best Christmas Movies', self.browser.title)

        # He is asked to start a new list
        list_inputbox = self.browser.find_element(By.ID, 'id_new_movie')

        list_inputbox.send_keys('Max Mustermann')

        list_inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)
        #self.assertEqual('Max Mustermann\'s Christmas Movie List', self.browser.find_element(By.ID, 'list-title').text)

        # Add movie
        movie_inputbox = self.browser.find_element(By.ID, 'id_new_movie')
        movie_inputbox.send_keys('Die Hard')
        movie_inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)
        self.assertEqual('Die Hard', self.browser.find_element(By.ID, 'movie-poster').get_attribute("alt"))

        # Select a movie
        movie_button = self.browser.find_element(By.ID, 'movie-button')
        movie_button.click()
        time.sleep(DEMO_MODE)
        self.assertEqual('Die Hard', self.browser.find_element(By.ID, 'movie-poster').get_attribute("alt"))
 """


