from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ChallengingDom(BasePage):
    HEAD_LINE = "h3"
    BUTTON = "//a[@class='button']"
    BUTTON_ALERT = "//a[@class='button alert']"
    BUTTON_SUCCESS = "//a[@class='button success']"
    TABLE_HEADER = "//table/thead/tr/th"
    TABLE_BODY = "//table/tbody/tr"
    TABLE = "//table"
    CANVAS = "canvas"

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

    def get_table(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.TABLE))
        )

    def get_table_header(self):
        return self._driver.find_elements(By.XPATH, self.TABLE_HEADER)

    def get_table_body(self):
        return self._driver.find_elements(By.XPATH, self.TABLE_BODY)

    def canvas(self):
        return self._driver.find_element(By.ID, self.CANVAS)
