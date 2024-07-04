from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ChallengingDom(BasePage):

    HEAD_LINE = "h3"
    BUTTON = "//a[@class='button']"
    BUTTON_ALERT = "//a[@class='button alert']"
    BUTTON_SUCCESS = "//a[@class='button success']"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/challenging_dom'

    def load(self):
        self._driver.get(self.url)

    def head_line(self):
        headline = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.HEAD_LINE))
        )
        return headline

    def click_button(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        )
        button.click()

    def click_alert_button(self):
        alert_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON_ALERT))
        )
        alert_button.click()

    def click_success_button(self):
        success_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.BUTTON_SUCCESS))
        )
        success_button.click()

