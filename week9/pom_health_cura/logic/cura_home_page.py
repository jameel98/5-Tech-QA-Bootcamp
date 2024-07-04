from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from week9.pom_health_cura.infra.base_page import BasePage


class HomePage(BasePage):
    BTN_MAKE_APPOINTMENT = "//button[@id='btn-make-appointment']"

    def __init__(self, driver):
        super.__init__(driver)
        self.url = 'https://katalon-demo-cura.herokuapp.com/'

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
