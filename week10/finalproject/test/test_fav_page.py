import unittest
from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.favorite_page import FavoritePage
from week10.finalproject.logic.pages.item_page import ItemPage
from week10.finalproject.logic.pages.login_page import Login
from week10.finalproject.infra.logger_setup import LogSetup  # Import the LogSetup class


class TestFavPage(unittest.TestCase):

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
        self.navbar = NavBar(self.driver)
        self.navbar.click_signin_button()
        self.login_page = Login(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.navbar.refresh_page()

        # Search for an item
        self.logger.info(f"Searching for item: {self.config['search_text_input']}.")
        self.navbar.search_item_by_text_flow(self.config["search_text_input"])
        self.app_page = BaseAppPage(self.driver)

        # Click on the searched item
        self.logger.info("Clicking on the searched item.")
        self.app_page.click_on_element()

        # Initialize the item page
        self.item_page = ItemPage(self.driver)

    def tearDown(self):
        # Log the quitting of WebDriver
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_add_item_to_favorite_page(self):
        # Arrange
        self.logger.info("Starting test_add_item_to_favorite_page.")

        # Save item details
        self.logger.info("Getting item details.")
        item = self.item_page.get_item_details()

        # Act
        self.logger.info("Adding item to the favorite list.")
        self.item_page.click_add_to_favorite_list()

        self.logger.info("Navigating to the favorite page.")
        self.navbar.click_fav_page_button()
        self.fav_page = FavoritePage(self.driver)

        # Get item details from the favorite page
        self.logger.info("Getting item details from the favorite page.")
        item2 = self.fav_page.get_item_details(1)

        # Assert
        self.logger.info("Asserting item details.")
        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)

    def test_remove_item_from_favorite_page(self):
        # Arrange
        self.logger.info("Starting test_remove_item_from_favorite_page.")

        # Add item to the favorite list
        self.logger.info("Adding item to the favorite list.")
        self.item_page.click_add_to_favorite_list()

        self.logger.info("Navigating to the favorite page.")
        self.navbar.click_fav_page_button()
        self.fav_page = FavoritePage(self.driver)

        # Act
        self.logger.info("Removing item from the favorite list.")
        self.fav_page.remove_item(1)

        # Assert
        self.logger.info("Asserting the favorite list is empty.")
        self.assertEqual(self.fav_page.empty_list_message().text, Messages.EMPTY_FAV_PAGE)

