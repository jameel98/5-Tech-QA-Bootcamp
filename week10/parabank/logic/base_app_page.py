from selenium.webdriver.common.by import By

from week10.parabank.infra.base_page import BasePage


class BaseAppPage(BasePage):

    NAME_INPUT = '//div[@class="login"]/name[@type="username"]'
    PASSWORD_INPUT = '//div[@class="login"]/name[@type="password"]'
    REGISTER = '//a[text()="Register"]'
    LOGIN = '//div[@class="login"]/input[@class="button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self._driver.get(self.get_config()["base_url"])

    def user_name_input(self):
        return self._driver.find_element(By.XPATH, self.NAME_INPUT)

    def password_input(self):
        return self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def register_button(self):
        return self._driver.find_element(By.XPATH, self.REGISTER)

    def login_button(self):
        return self._driver.find_element(By.XPATH, self.LOGIN)
    
