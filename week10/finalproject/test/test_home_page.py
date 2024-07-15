import time
import unittest
from selenium.webdriver import Keys
from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.infra.logger_setup import LogSetup
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.enums.outer_category import OuterCategory
from week10.finalproject.logic.enums.sports import Sports


class TestHomePage(unittest.TestCase):

    def setUp(self):
        """
        setup for home page tests
        initialize browser
        initialize page components
        login with valid email and password
        :return:
        """
        # Instantiate the logger
        log_setup = LogSetup()
        self.logger = log_setup.logger

        # initialization of BrowserWrapper and WebDriver
        self.logger.info("Initializing BrowserWrapper and WebDriver.")
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])

        # initialization of page components
        self.app_page = BaseAppPage(self.driver)
        self.navbar = NavBar(self.driver)

    def tearDown(self):
        # Log the quitting of WebDriver
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_search_item_by_name(self):
        """
        search item by name
        get name from config file and send it
        to search function
        validate item exist in result list
        :return:
        """
        # Arrange
        self.logger.info("Starting test_search_item_by_name.")

        # clicking the search text button
        self.navbar.click_search_text_button()

        # entering search text
        search_box = self.navbar.get_search_text_input()
        search_box.send_keys(self.config["search_text_input"])

        # Act
        # click on search button
        search_box.send_keys(Keys.ENTER)

        # Assert
        self.assertTrue(self.app_page.get_search_results(self.config["search_text_input"]))

    def test_search_by_category(self):
        """
        search item by category
        hover over category name
        pick category
        """
        # Arrange
        self.logger.info("Starting test_search_by_category.")
        self.navbar.hover_over_outer_category(OuterCategory.SPORTS)

        # Act
        # click on the category
        self.navbar.click_on_inner_category(Sports.TRAINING)

        # Assert
        self.assertTrue(self.app_page.get_search_results(Sports.TRAINING))

