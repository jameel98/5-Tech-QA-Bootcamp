from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week9.pom_health_cura.infra.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME_INPUT = '//input[@id="txt-username"]'
    PASSWORD_INPUT = '//input[@id="txt-password"]'
    LOGIN_BUTTON = '//input[@id="btn-login"]'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)


    def initialize_locators(self):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        user_input.click()
