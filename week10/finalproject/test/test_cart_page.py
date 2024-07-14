import unittest
from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.cart_pop_up import CartPopup
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.cart_page import CartPage
from week10.finalproject.logic.pages.item_page import ItemPage
from week10.finalproject.logic.pages.login_page import Login
from week10.finalproject.infra.logger_setup import LogSetup  # Import the LogSetup class


class TestCartPage(unittest.TestCase):

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
        self.logger.info("Clicking the sign-in button.")
        self.navbar.click_signin_button()
        self.login_page = Login(self.driver)
        self.logger.info("Performing login flow.")
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.logger.info("Refreshing the page.")
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

    def test_add_item_to_cart_page(self):
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_page.")

        # Save item details
        self.logger.info("Getting item details.")
        item = self.item_page.get_item_details()

        # Act
        self.logger.info("Adding item to the cart list.")
        self.item_page.click_add_to_cart_list()

        self.logger.info("Navigating to the cart page.")
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)

        # Get item details from the cart page
        self.logger.info("Getting item details from the cart page.")
        item2 = self.cart_page.get_item_details(1)

        # Assert
        self.logger.info("Asserting item details.")
        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)

    def test_add_item_to_cart_without_size(self):
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_without_size.")

        # Save item details without size
        self.logger.info("Getting item details without size.")
        self.item_page.get_item_details_no_size()

        # Act
        self.logger.info("Attempting to add item to the cart list without selecting size.")
        self.item_page.click_add_to_cart_list()

        # Assert
        self.logger.info("Asserting size error message.")
        self.assertEqual(self.item_page.get_size_error_message().text, Messages.SIZE_ERROR)

    def test_add_item_to_cart_without_color(self):
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_without_color.")

        # Save item details without color
        self.logger.info("Getting item details without color.")
        self.item_page.get_item_details_no_color()

        # Act
        self.logger.info("Attempting to add item to the cart list without selecting color.")
        self.item_page.click_add_to_cart_list()

        # Assert
        self.logger.info("Asserting color error message.")
        self.assertEqual(self.item_page.get_color_error_message().text, Messages.COLOR_ERROR)

    def test_remove_item_from_cart_page(self):
        # Arrange
        self.logger.info("Starting test_remove_item_from_cart_page.")

        # Save item details
        self.logger.info("Getting item details.")
        self.item_page.get_item_details()

        # Add item to the cart list
        self.logger.info("Adding item to the cart list.")
        self.item_page.click_add_to_cart_list()

        self.logger.info("Navigating to the cart page.")
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)

        # Act
        self.logger.info("Removing item from the cart page.")
        self.cart_page.remove_item(1)

        # Assert
        self.logger.info("Asserting the cart page is empty.")
        self.assertEqual(self.cart_page.empty_list_message().text, Messages.EMPTY_CART_PAGE)

