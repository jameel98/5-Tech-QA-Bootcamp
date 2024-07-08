from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.parabank.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SIGNIN_BUTTON = '//div[@id="buttons"]/ytd-button-renderer'
    AVATAR = "//img[@id='img' and @alt='Avatar image']"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self._driver.get(self.get_config()["base_url"])

    def sign_in_button(self):
        wait = WebDriverWait(self._driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON)))
        return element

    def get_avatar(self):
        return self._driver.find_element(By.XPATH, self.AVATAR)

