import unittest

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.favorite_page import FavoritePage
from week10.finalproject.logic.pages.item_page import ItemPage
from week10.finalproject.logic.pages.login_page import Login


class TestFavPage(unittest.TestCase):

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

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_favorite_page(self):
        # arrange
        # search item
        self.navbar = NavBar(self.driver)
        self.navbar.search_item_by_text_flow(self.config["search_text_input"])
        self.app_page = BaseAppPage(self.driver)
        items = self.app_page.get_elements_list()
        items[0].click()

        # save item details
        self.item_page = ItemPage(self.driver)
        item = self.item_page.get_item_details()

        # act
        self.item_page.click_add_to_favorite_list()

        # assert
        self.navbar.click_fav_page_button()
        self.fav_page = FavoritePage(self.driver)
        item2 = self.fav_page.get_item_details(1)

        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)
        self.assertEqual(item._size, item2._size)
        self.assertEqual(item._color, item2._color)



