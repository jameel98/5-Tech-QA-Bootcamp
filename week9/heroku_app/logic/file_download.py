from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week9.heroku_app.infra.base_page import BasePage


class FileDownload(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/download'

    def load(self):
        self._driver.get(self.url)

    def download_file(self, num):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@class="example"]/a[{num}]'))
        )
        button.click()
