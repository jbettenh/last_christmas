import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time

MAX_WAIT = 10


class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server: os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()