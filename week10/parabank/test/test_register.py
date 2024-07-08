import unittest

from week10.parabank.infra.browser_wrapper import BrowserWrapper
from week10.parabank.infra.config_provider import ConfigProvider
from week10.parabank.logic.base_app_page import BaseAppPage
from week10.parabank.logic.register import Register


class TestRegister(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.driver.maximize_window()
        self.app_page = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        self.app_page.register_button().click()
        self.register_page = Register(self.driver)

        self.register_page.get_first_name().send_keys("jameel")
        self.register_page.get_last_name().send_keys("mograbi")
        self.register_page.get_address().send_keys("asdfdf")
        self.register_page.get_city().send_keys("ein kynia")
        self.register_page.get_state().send_keys("golan")
        self.register_page.get_zip_code().send_keys("1243200")
        self.register_page.get_phone().send_keys("0502694219")
        self.register_page.get_ssn().send_keys("0502694219")
        self.register_page.get_user_name().send_keys("jim")
        self.register_page.get_password().send_keys("abc1234")
        self.register_page.get_confirm().send_keys("abc1234")
        self.register_page.get_register().click()
