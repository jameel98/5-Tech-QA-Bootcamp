import unittest
import undetected_chromedriver as uc

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.infra.utils import Utils
from week10.finalproject.logic.base_app_page import BaseAppPage


class TestRegister(unittest.TestCase):

    def setUp(self):
        # Initialize the undetected ChromeDriver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.app_page = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

