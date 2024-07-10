import time
import unittest

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.base_app_page import BaseAppPage


class TestHomePage(unittest.TestCase):

    def setUp(self):
        # Initialize the undetected ChromeDriver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.driver.maximize_window()
        self.app_page = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_item_by_name(self):
        self.app_page.search_item_by_text(self.config["search_text_input"])
        time.sleep(5)
        self.assertTrue(self.app_page.get_search_results())

