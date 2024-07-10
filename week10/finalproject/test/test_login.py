import unittest
import undetected_chromedriver as uc

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.infra.utils import Utils
from week10.finalproject.logic.base_app_page import BaseAppPage
from week10.finalproject.logic.login_page import Login


class TestLogin(unittest.TestCase):

    def setUp(self):
        # Initialize the undetected ChromeDriver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.app_page = BaseAppPage(self.driver)
        self.app_page.sign_in_button().click()
        self.login_page = Login(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_successfully(self):
        self.login_page.login_flow(self.config["email"], self.config["password"])

        self.assertIsNotNone(self.app_page.get_avatar())

    def test_login_unsuccessfully(self):
        self.login_page.login_flow(self.config["email"], Utils.generate_random_string(5))

        self.assertIsNone(self.app_page.get_avatar())

