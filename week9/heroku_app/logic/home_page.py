from selenium.webdriver.common.by import By

from week9.heroku_app.infra.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/'

    def load(self):
        self._driver.get(self.url)

    def get_all_links(self):
        return self._driver.find_elements(By.XPATH, "//li")

