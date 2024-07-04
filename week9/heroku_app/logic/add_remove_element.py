from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AddRemoveElement(BasePage):

    HEAD_LINE = "h3"

    ADD_BUTTON = '//button[text()="Add Element"]'
    REMOVE_BUTTON = '//button[text()="Delete"]'
    ELEMENTS_LIST = '//button[@class="added-manually"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/add_remove_elements/'

    def load(self):
        self._driver.get(self.url)

    def head_line(self):
        headline = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.HEAD_LINE))
        )
        return headline

    def add_element(self):
        add_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ADD_BUTTON))
        )
        add_button.click()

    def get_elements_list(self):
        return self._driver.find_elements(By.XPATH, self.ELEMENTS_LIST)

