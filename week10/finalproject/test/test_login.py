import unittest

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.infra.utils import Utils
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.logic.pages.login_page import Login


class TestLogin(unittest.TestCase):

    def setUp(self):
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        # initialize pages
        self.navbar = NavBar(self.driver)
        self.navbar.click_signin_button()
        self.login_page = Login(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_successfully(self):
        # arrange
        self.login_page.fill_email_input(self.config["email"])
        self.login_page.fill_password_input(self.config["password"])
        # act
        self.login_page.click_login()
        # assert
        self.assertIsNotNone(self.navbar.get_avatar())

    def test_login_unsuccessfully(self):
        # arrange
        self.login_page.fill_email_input(self.config["email"])
        self.login_page.fill_password_input(Utils.generate_random_string(5))
        # act
        self.login_page.click_login()
        # assert
        self.assertEqual(self.login_page.get_error_message().text, "אימייל או סיסמה שגויים")

