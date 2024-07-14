import unittest

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
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

        # search element
        self.navbar.search_item_by_text_flow(self.config["search_text_input"])
        self.app_page = BaseAppPage(self.driver)
        # click element
        self.app_page.click_on_element()
        # init item page
        self.item_page = ItemPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_favorite_page(self):
        # arrange
        # save item details
        item = self.item_page.get_item_details()

        # act
        # add item to fav list
        self.item_page.click_add_to_favorite_list()

        # go to fav page
        self.navbar.click_fav_page_button()
        self.fav_page = FavoritePage(self.driver)

        # get item details
        item2 = self.fav_page.get_item_details(1)

        # assert
        self.assertEqual(item._name, item2._name)
        self.assertEqual(item._final_price, item2._final_price)

    def test_remove_item_from_favorite_page(self):
        # arrange
        # add item to fav list
        self.item_page.click_add_to_favorite_list()
        # go to fav page
        self.navbar.click_fav_page_button()
        self.fav_page = FavoritePage(self.driver)

        # act
        self.fav_page.remove_item(1)

        # assert
        self.assertEqual(self.fav_page.empty_list_message().text, Messages.EMPTY_FAV_PAGE)

