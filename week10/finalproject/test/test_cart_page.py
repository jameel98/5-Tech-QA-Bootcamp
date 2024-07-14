import unittest

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.cart_pop_up import CartPopup
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.cart_page import CartPage
from week10.finalproject.logic.pages.item_page import ItemPage
from week10.finalproject.logic.pages.login_page import Login


class TestCartPage(unittest.TestCase):

    def setUp(self):
        # Initialize the driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.driver.maximize_window()

        # Initialize the pages
        self.navbar = NavBar(self.driver)
        self.navbar.click_signin_button()
        self.login_page = Login(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])
        self.navbar.refresh_page()
        # search element
        self.navbar.search_item_by_text_flow(self.config["search_text_input"])
        self.app_page = BaseAppPage(self.driver)
        self.app_page.click_on_element()
        self.item_page = ItemPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_cart_page(self):
        # arrange
        # save item details
        item = self.item_page.get_item_details()

        # act
        # add item to cart list
        self.item_page.click_add_to_cart_list()

        # go to cart page
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)
        # get item details
        item2 = self.cart_page.get_item_details(1)

        # assert
        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)

    def test_add_item_to_cart_without_size(self):
        # arrange
        # save item details
        self.item_page.get_item_details_no_size()

        # act
        # add item to cart list
        self.item_page.click_add_to_cart_list()
        # assert
        self.assertEqual(self.item_page.get_size_error_message().text, Messages.SIZE_ERROR)

    def test_add_item_to_cart_without_color(self):
        # arrange
        # save item details
        self.item_page.get_item_details_no_color()

        # act
        # add item to cart list
        self.item_page.click_add_to_cart_list()
        # assert
        self.assertEqual(self.item_page.get_color_error_message().text, Messages.COLOR_ERROR)

    def test_remove_item_from_cart_page(self):
        # arrange
        # save item details
        self.item_page.get_item_details()
        # add item to cart list
        self.item_page.click_add_to_cart_list()
        # go to cart page
        self.cart_pop = CartPopup(self.driver)
        self.cart_pop.click_cart_button()
        self.cart_page = CartPage(self.driver)

        # act
        self.cart_page.remove_item(1)

        # assert
        self.assertEqual(self.cart_page.empty_list_message().text, Messages.EMPTY_CART_PAGE)
