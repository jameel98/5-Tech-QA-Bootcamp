from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com'
        self.search_box_name = 'q'

    def load(self):
        self.driver.get(self.url)

    def enter_search_query(self, query):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.search_box_name))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
