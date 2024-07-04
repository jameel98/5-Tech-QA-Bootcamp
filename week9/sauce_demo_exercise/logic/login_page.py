from selenium.webdriver.common.by import By
from week9.sauce_demo_exercise.infra.base_page import BasePage


class LoginPage(BasePage):
    HOME_HEADER_TEXT = '//div[@class="login_logo"]'
    USER_NAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id= "login-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        self._home_header_text = self._driver.find_element(By.XPATH, self.HOME_HEADER_TEXT)

        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def load(self):
        self._driver.get(self.url)

    def fill_user_input(self, username):
        self._user_name_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_login_button(self):
        self._login_button.click()

    def login_flow(self, username, password):
        self.fill_user_input(username)
        self.fill_password_input(password)
        self.click_login_button()
