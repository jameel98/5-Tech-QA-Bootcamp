import unittest
from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.cart_pop_up import CartPopup
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.cart_page import CartPage
from week10.finalproject.logic.pages.item_page import ItemPage
from week10.finalproject.logic.pages.login_page import Login
from week10.finalproject.infra.logger_setup import LogSetup


class TestCartPage(unittest.TestCase):

    def setUp(self):
        """
        setup for cart tests initialize browser
        initialize page components
        login with valid email and password
        search for item by his name
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
        self.driver.maximize_window()

        # initialization of page components
        self.logger.info("Initializing page components.")
        self.navbar = NavBar(self.driver)
        self.navbar.click_signin_button()
        # login
        self.login_page = Login(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.navbar.refresh_page()

        # Search for an item
        self.logger.info(f"Searching for item: {self.config['search_text_input']}.")
        self.navbar.search_item_by_text_flow(self.config["search_text_input"])
        self.app_page = BaseAppPage(self.driver)

        # Click on the searched item
        self.app_page.click_on_element()

        # Initialize the item page
        self.item_page = ItemPage(self.driver)

    def tearDown(self):
        # Log the quitting of WebDriver
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_add_item_to_cart_page(self):
        """
        test add item to cart page it save item details in item object
        then click on add item to cart and navigate to cart page
        validates the item is added
        :return:
        """
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_page.")
        # Save item details
        item = self.item_page.get_item_details()
        # Act
        self.item_page.click_add_to_cart_list()

        # navigate to the cart page
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)
        # Get item details from the cart page
        item2 = self.cart_page.get_item_details(1)

        # Assert
        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)

    def test_add_item_to_cart_without_size(self):
        """
        negative test add item to cart page without choosing its size
        it save item details in item object
        then click on add item to cart
        validates the missing size message displayed
        :return:
        """
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_without_size.")

        # Save item details without size
        self.item_page.get_item_details_no_size()

        # Act
        # add item to cart
        self.item_page.click_add_to_cart_list()

        # Assert
        self.assertEqual(self.item_page.get_size_error_message().text, Messages.SIZE_ERROR)

    def test_add_item_to_cart_without_color(self):
        """
        negative test add item to cart page without choosing its size
        it save item details in item object
        then click on add item to cart
        validates the missing color message displayed
        :return:
        """
        # Arrange
        self.logger.info("Starting test_add_item_to_cart_without_color.")

        # Save item details without color
        self.item_page.get_item_details_no_color()

        # Act
        # click add item to cart
        self.item_page.click_add_to_cart_list()

        # Assert
        self.assertEqual(self.item_page.get_color_error_message().text, Messages.COLOR_ERROR)

    def test_remove_item_from_cart_page(self):
        """
        test remove item from cart page
        it save item details in item object
        then click on add item to cart
        navigate to cart page
        remove the item
        validates no items in cart page
        :return:
        """
        # Arrange
        self.logger.info("Starting test_remove_item_from_cart_page.")
        # Save item details
        self.item_page.get_item_details()
        # Add item to the cart list
        self.item_page.click_add_to_cart_list()
        # navigate to cart page
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)

        # Act
        self.cart_page.remove_item(1)

        # Assert
        self.assertEqual(self.cart_page.empty_list_message().text, Messages.EMPTY_CART_PAGE)
