import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time

MAX_WAIT = 10


class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        time.sleep(3)
        self.assertEqual('The Best Christmas Movies', self.browser.title)
