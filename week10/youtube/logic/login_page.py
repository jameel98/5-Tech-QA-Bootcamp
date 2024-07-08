from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from week10.youtube.infra.config_provider import ConfigProvider
from week10.youtube.logic.base_app_page import BaseAppPage


class Login(BaseAppPage):
    EMAIL_INPUT = "//input[@type='email']"
    PASSWORD_INPUT = "//input[@type='password']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_email_input(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL_INPUT)))

    def get_password_input(self):
        wait = WebDriverWait(self._driver, 20)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT)))

    def login_flow(self, email, password):

        # Enter the email
        email_input = self.get_email_input()
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)

        # Wait for the password field to load
        time.sleep(2)

        # Enter the password
        password_input = self.get_password_input()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        # Wait for the login process to complete
        time.sleep(5)

