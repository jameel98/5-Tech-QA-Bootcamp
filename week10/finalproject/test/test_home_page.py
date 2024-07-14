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
        # Instantiate the logger
        log_setup = LogSetup()
        self.logger = log_setup.logger

        # Log the initialization of BrowserWrapper and WebDriver
        self.logger.info("Initializing BrowserWrapper and WebDriver.")
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.driver.maximize_window()

        # Log the initialization of page components
        self.logger.info("Initializing page components.")
        self.app_page = BaseAppPage(self.driver)
        self.navbar = NavBar(self.driver)

    def tearDown(self):
        # Log the quitting of WebDriver
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_search_item_by_name(self):
        # Arrange
        self.logger.info("Starting test_search_item_by_name.")

        # Log clicking the search text button
        self.logger.info("Clicking the search text button.")
        self.navbar.click_search_text_button()

        # Log entering search text
        self.logger.info(f"Entering search text: {self.config['search_text_input']}.")
        search_box = self.navbar.get_search_text_input()
        search_box.send_keys(self.config["search_text_input"])

        # Act
        self.logger.info("Sending Enter key to search box.")
        search_box.send_keys(Keys.ENTER)

        # Assert
        self.logger.info(f"Asserting search results for: {self.config['search_text_input']}.")
        self.assertTrue(self.app_page.get_search_results(self.config["search_text_input"]))

    def test_search_by_category(self):
        # Arrange
        self.logger.info("Starting test_search_by_category.")
        self.logger.info(f"Hovering over outer category: {OuterCategory.SPORTS}.")
        self.navbar.hover_over_outer_category(OuterCategory.SPORTS)

        # Act
        self.logger.info(f"Clicking on inner category: {Sports.TRAINING}.")
        self.navbar.click_on_inner_category(Sports.TRAINING)

        # Assert
        self.logger.info(f"Asserting search results for category: {Sports.TRAINING}.")
        self.assertTrue(self.app_page.get_search_results(Sports.TRAINING))

