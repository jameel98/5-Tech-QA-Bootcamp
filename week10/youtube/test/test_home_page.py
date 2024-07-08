import unittest
import undetected_chromedriver as uc
from week10.youtube.infra.browser_wrapper import BrowserWrapper
from week10.youtube.infra.config_provider import ConfigProvider
from week10.youtube.logic.base_app_page import BaseAppPage
from week10.youtube.logic.login_page import Login


class TestRegister(unittest.TestCase):

    def setUp(self):
        # Initialize the undetected ChromeDriver
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        self.config = ConfigProvider.load_from_file('../config.json')
        self.driver.get(self.config["base_url"])
        self.app_page = BaseAppPage(self.driver)
        self.app_page.sign_in_button().click()
        self.login_page = Login(self.driver)
        self.login_page.login_flow()

    def tearDown(self):
        self.driver.quit()

    def test_nothing(self):
        print("login success")
