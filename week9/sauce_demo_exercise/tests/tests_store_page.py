import unittest

from week9.sauce_demo_exercise.infra.web_driver import WebDriverSetup
from week9.sauce_demo_exercise.logic.cart_page import ShoppingCartPage
from week9.sauce_demo_exercise.logic.login_page import LoginPage
from week9.sauce_demo_exercise.logic.main_page import MainPage


class TestStorePage(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriverSetup().get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_2_items_to_cart(self):
        self.login_page.login_flow('standard_user', 'secret_sauce')
        self.main_page = MainPage(self.driver)
        self.main_page.add_item_to_cart(self.main_page.BACK_PACK)
        self.main_page.add_item_to_cart(self.main_page.BIKE_LIGHTS)
        self.main_page.click_cart_button()
        self.cart_page = ShoppingCartPage(self.driver)
        self.assertEqual(len(self.cart_page.get_cart_items()), 2)

    def test_add_3_remove_1_item(self):
        self.login_page.login_flow('standard_user', 'secret_sauce')
        self.main_page = MainPage(self.driver)
        self.main_page.add_item_to_cart(self.main_page.BACK_PACK)
        self.main_page.add_item_to_cart(self.main_page.BIKE_LIGHTS)
        self.main_page.add_item_to_cart(self.main_page.BOLT_T_SHIRT)
        self.main_page.click_cart_button()
        self.cart_page = ShoppingCartPage(self.driver)
        self.cart_page.remove_item_from_cart(self.main_page.BOLT_T_SHIRT)

        self.assertEqual(len(self.cart_page.get_cart_items()), 2)

    def test_cart_not_empty_after_logout(self):
        self.login_page.login_flow('standard_user', 'secret_sauce')
        self.main_page = MainPage(self.driver)
        self.main_page.add_item_to_cart(self.main_page.BACK_PACK)
        self.main_page.side_menu.logout()

        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow('standard_user', 'secret_sauce')

        self.main_page = MainPage(self.driver)
        self.main_page.click_cart_button()

        self.cart_page = ShoppingCartPage(self.driver)

        self.assertEqual(len(self.cart_page.get_cart_items()), 1)
