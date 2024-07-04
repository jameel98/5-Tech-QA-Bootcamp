from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class UltimatePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://ultimateqa.com/simple-html-elements-for-automation/'
        self.btn_click_me_loc = "//button[@id='button1']"
        self.btn_id_loc = "//a[@id='idExample']"
        self.success_message_loc = "//h1[@class='entry-title' and text()='Button success']"
        self.radio_btn_loc ="//form//input[@value=\"male\"]"

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