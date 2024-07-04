from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    # Always get driver
    def __init__(self, driver):
        self._driver = driver

    def load(self):
        self._driver.get(self.url)

    def refresh_page(self):
        self._driver.reload()

    def find_element(self, locator):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )

    def find_elements(self, locator):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )
