from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week9.heroku_app.infra.base_page import BasePage


class FileUpload(BasePage):

    UPLOAD_BUTTON = '//input[@id="file-upload"]'
    SUBMIT_BUTTON = '//input[@id="file-submit"]'
    SUCCESS_MESSAGE = 'h3'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/upload'

    def load(self):
        self._driver.get(self.url)

    def upload_button(self):
        return WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UPLOAD_BUTTON))
        )

    def submit_button(self):
        return WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON))
        )

    def get_success_message(self):
        return WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUCCESS_MESSAGE))
        )
