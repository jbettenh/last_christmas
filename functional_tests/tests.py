import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10
DEMO_MODE = 7


class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)

        self.assertEqual('The Best Christmas Movies', self.browser.title)

        # He is asked to start a new list
        inputbox = self.browser.find_element(By.ID, 'id_new_movie')

        inputbox.send_keys('Max Mustermann')
      
        inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)

        # Add movie
        inputbox = self.browser.find_element(By.ID, 'id_new_movie')
        inputbox.send_keys('Home Alone')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(DEMO_MODE)

        # Select a movie


