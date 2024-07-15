import unittest
from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from week10.finalproject.infra.logger_setup import LogSetup
from week10.finalproject.infra.utils import Utils
from week10.finalproject.logic.components.navbar import NavBar
from week10.finalproject.logic.enums.messages import Messages
from week10.finalproject.logic.pages.login_page import Login


class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        setup initialize browser data
        initialize pages before tests run
        :return:
        """
        # Instantiate the logger
        log_setup = LogSetup()
        self.logger = log_setup.logger

        # Initialize driver
        self.logger.info("Initializing BrowserWrapper and WebDriver.")
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])

        # Initialize pages
        self.navbar = NavBar(self.driver)
        self.navbar.click_signin_button()
        self.login_page = Login(self.driver)

    def tearDown(self):
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_login_successfully(self):
        """
        login successful with valid email and password
        click login in navbar
        popup appear so put input and click login
        wait to popup disappear and validate username appears
        :return:
        """
        # Arrange
        self.logger.info("test login successfully starts.")
        self.login_page.fill_email_input(self.config["email"])
        self.login_page.fill_password_input(self.config["password"])

        # Act
        # click on login
        self.login_page.click_login()

        # Assert
        self.assertIsNotNone(self.navbar.get_avatar())

    def test_login_unsuccessfully(self):
        """
        login unsuccessful with invalid password
        click login in navbar
        popup appear so put input and click login
        validate error message "invalid email or password" appears
        :return:
        """
        # Arrange
        self.logger.info("login unsuccessfully started.")
        self.login_page.fill_email_input(self.config["email"])
        self.login_page.fill_password_input(Utils.generate_random_string(5))

        # Act
        # click on login
        self.login_page.click_login()

        # Assert
        self.assertEqual(self.login_page.get_error_message().text, Messages.EMAIL_ERROR)
