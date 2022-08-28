from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth import get_user_model
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumlogin import force_login
import time

from last_christmas import __version__

MAX_WAIT = 10
DEMO_MODE = 1

def test_version():
    assert __version__ == '1.2.0'

class NewVistorTest(LiveServerTestCase):
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


    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentallz tries to submit an empty list item
        # She hits enter on the empty list box
        # The home page refreshes, and there is an error message saying that list items cannot be blank
        # She tries again with some text for the item, which now works
        # Perversely, she now decides to submit a second blank list item
        # She receives a similar warning on the list page
        # And she can correct it by filling some text in
        self.fail('write me!')