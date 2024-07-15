from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from week10.youtube.logic.base_app_page import BaseAppPage
from week10.finalproject.infra.logger_setup import LogSetup


class Login(BaseAppPage):
    # locators
    EMAIL_INPUT_LOC = "//input[@id='qa-login-email-input']"
    PASSWORD_INPUT_LOC = "//input[@id='qa-login-password-input']"
    LOGIN_BUTTON_LOC = "//button[@data-test-id='qa-login-submit']"
    ERROR_MESSAGE_LOC = "//div[@class='error-message_3NOI']"

    def __init__(self, driver):
        super().__init__(driver)
        # init logger
        log_setup = LogSetup()
        self.logger = log_setup.logger
        # find element
        wait = WebDriverWait(self._driver, 10)
        try:
            self.email_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL_INPUT_LOC)))
            self.password_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT_LOC)))
            self.login_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_LOC)))
        except Exception as e:
            self.logger.error(f"Error initializing Login page elements: {e}")
            raise

    def fill_email_input(self, email):
        """
        this function fills the email input
        :param email: gets email input parameter and puts is in email field
        :return:
        """
        try:
            self.logger.info(f"Entering email: {email}")
            self.email_input.send_keys(email)
        except Exception as e:
            self.logger.error(f"Error entering email: {e}")
            raise

    def fill_password_input(self, password):
        """
        this function fills the password input
        :param password: gets email input parameter and puts is in password field
        :return:
        """
        try:
            self.logger.info(f"Entering password.")
            self.password_input.send_keys(password)
        except Exception as e:
            self.logger.error(f"Error entering password: {e}")
            raise

    def click_login(self):
        """
        this function click on the login button
        :return:
        """
        try:
            self.logger.info("Clicking the login button.")
            self.login_button.click()
        except Exception as e:
            self.logger.error(f"Error clicking login button: {e}")
            raise

    def get_error_message(self):
        """
        this function search for error message
        :return: error message element
        """
        try:
            self.logger.info("Waiting for error message to be visible.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting error message: {e}")
            raise

    def login_flow(self, email, password):
        """
        this is login flow function used to login, helpful
        to do all the login in one function
        :param email:
        :param password:
        :return:
        """
        try:
            self.logger.info("Starting login flow.")
            self.fill_email_input(email)
            self.fill_password_input(password)
            self.click_login()
        except Exception as e:
            self.logger.error(f"Error during login flow: {e}")
            raise
