from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from week10.youtube.logic.base_app_page import BaseAppPage


class Login(BaseAppPage):
    EMAIL_INPUT_LOC = "//input[@id='qa-login-email-input']"
    PASSWORD_INPUT_LOC = "//input[@id='qa-login-password-input']"
    LOGIN_BUTTON_LOC = "//button[@data-test-id='qa-login-submit']"
    ERROR_MESSAGE_LOC = "//div[@class='error-message_3NOI']"

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        self.email_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL_INPUT_LOC)))
        self.password_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT_LOC)))
        self.login_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_LOC)))

    def fill_email_input(self, email):
        # Enter the email
        self.email_input.send_keys(email)

    def fill_password_input(self, password):
        # Enter the password
        self.password_input.send_keys(password)

    def click_login(self):
        self.login_button.click()

    def get_error_message(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.ERROR_MESSAGE_LOC)))

    def login_flow(self, email, password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_login()



