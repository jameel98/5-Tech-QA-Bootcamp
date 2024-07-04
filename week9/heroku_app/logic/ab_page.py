from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ABPage(BasePage):
    HEAD_LINE = "h3"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/abtest'

    def load(self):
        self._driver.get(self.url)

    def head_line(self):
        headline = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.HEAD_LINE))
        )
        return headline

