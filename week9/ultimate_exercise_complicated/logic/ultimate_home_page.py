from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UltimatePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://ultimateqa.com/complicated-page/'

    def load(self):
        self.driver.get(self.url)

    def click_btn(self, locator):
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        btn.click()

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element.text
