from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckBoxes(BasePage):
    HEAD_LINE = "h3"

    CHECK_BOX1 = "//form[@id='checkboxes']/input[1]"
    CHECK_BOX2 = "//form[@id='checkboxes']/input[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/checkboxes'

    def load(self):
        self._driver.get(self.url)

    def head_line(self):
        headline = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.HEAD_LINE))
        )
        return headline

    def click_check_box1(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHECK_BOX1))
        )
        if not button.is_selected():
            button.click()

    def unclick_check_box1(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHECK_BOX1))
        )
        if button.is_selected():
            button.click()

