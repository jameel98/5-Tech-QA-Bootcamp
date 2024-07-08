from selenium.webdriver.common.by import By

from week10.parabank.logic.base_app_page import BaseAppPage


class Register(BaseAppPage):
    FIRST_NAME = '//input[@id="customer.firstName"]'
    LAST_NAME = '//input[@id="customer.lastName"]'
    ADDRESS = '//input[@id="customer.address.street"]'
    CITY = '//input[@id="customer.address.city"]'
    STATE = '//input[@id="customer.address.state"]'
    ZIP_CODE = '//input[@id="customer.address.zipCode"]'
    PHONE = '//input[@id="customer.phoneNumber"]'
    SSN = '//input[@id="customer.ssn"]'
    USER_NAME = '//input[@id="customer.username"]'
    PASSWORD = '//input[@id="customer.password"]'
    CONFIRM = '//input[@id="repeatedPassword"]'
    REGISTER = '//input[@value="Register"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_name(self):
        return self._driver.find_element(By.XPATH, self.FIRST_NAME)

    def get_last_name(self):
        return self._driver.find_element(By.XPATH, self.LAST_NAME)

    def get_address(self):
        return self._driver.find_element(By.XPATH, self.ADDRESS)

    def get_city(self):
        return self._driver.find_element(By.XPATH, self.CITY)

    def get_state(self):
        return self._driver.find_element(By.XPATH, self.STATE)

    def get_zip_code(self):
        return self._driver.find_element(By.XPATH, self.ZIP_CODE)

    def get_phone(self):
        return self._driver.find_element(By.XPATH, self.PHONE)

    def get_ssn(self):
        return self._driver.find_element(By.XPATH, self.SSN)

    def get_user_name(self):
        return self._driver.find_element(By.XPATH, self.USER_NAME)

    def get_password(self):
        return self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def get_confirm(self):
        return self._driver.find_element(By.XPATH, self.CONFIRM)

    def get_register(self):
        return self._driver.find_element(By.XPATH, self.REGISTER)
