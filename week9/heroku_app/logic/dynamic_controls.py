from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week9.heroku_app.infra.base_page import BasePage


class DynamicControls(BasePage):
    CHECK_BOX = "checkbox"
    REMOVE = '//button[text()="Remove"]'
    ADD = '//button[text()="Add"]'
    ENABLE_BUTTON = '//button[text()="Enable"]'
    DISABLE_BUTTON = '//button[text()="Enable"]'
    ENABLE_INPUT = '//input[@type="text"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/dynamic_controls'

    def load(self):
        self._driver.get(self.url)

    def click_checkbox(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHECK_BOX))
        )
        if not button.is_selected():
            button.click()

    def click_remove(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE))
        )
        button.click()

    def click_add(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD))
        )
        button.click()

    def click_enable(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ENABLE_BUTTON))
        )
        button.click()

    def click_disable(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DISABLE_BUTTON))
        )
        button.click()

    def write_input(self, text):
        input_text = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ENABLE_INPUT))
        )
        input_text.sendkeys(text)
