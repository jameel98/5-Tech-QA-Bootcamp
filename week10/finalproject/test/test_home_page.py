import time
import unittest

from selenium.webdriver import Keys

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.enums.outer_category import OuterCategory
from week10.finalproject.logic.enums.sports import Sports


class TestHomePage(unittest.TestCase):

    def setUp(self):
        # initialize the Driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.driver.maximize_window()
        # initialize pages
        self.app_page = BaseAppPage(self.driver)
        self.navbar = NavBar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_item_by_name(self):
        # arrange
        self.navbar.click_search_text_button()
        search_box = self.navbar.get_search_text_input()
        search_box.send_keys(self.config["search_text_input"])
        # act
        search_box.send_keys(Keys.ENTER)
        # assert
        self.assertTrue(self.app_page.get_search_results(self.config["search_text_input"]))

    def test_search_by_category(self):
        # act
        self.navbar.hover_over_outer_category(OuterCategory.SPORTS)
        self.navbar.click_on_inner_category(Sports.TRAINING)
        # assert
        self.app_page.get_search_results(Sports.TRAINING)
