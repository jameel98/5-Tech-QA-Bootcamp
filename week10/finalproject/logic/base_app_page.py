from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.parabank.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SIGNIN_BUTTON = '//div[text()="התחברות"]'
    AVATAR = '//span[@class="profile-button-new-menu-underline_1fv_"]'
    SEARCH_TEXT_BUTTON = '//button[@class="search-button_1ENs"]'
    SEARCH_TEXT_INPUT = '//input[@class="input_sILM"]'
    SEARCH_RESULTS = '//ol[@class="product-list_yyTm"]/li'

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self._driver.get(self.get_config()["base_url"])

    def sign_in_button(self):
        wait = WebDriverWait(self._driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON)))
        return element

    def get_avatar(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.AVATAR)))

    def get_search_text_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_BUTTON)))

    def get_search_text_input(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_INPUT)))

    def search_item_by_text(self, query):
        search_button = self.get_search_text_button()
        search_button.click()
        search_box = self.get_search_text_input()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def get_search_results(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_RESULTS))
        )
        results = self._driver.find_elements(By.XPATH, self.SEARCH_RESULTS)

        for i in range(1, len(results) + 1):
            element = self._driver.find_element(By.XPATH, self.SEARCH_RESULTS + f"[{i}]/div[2]")
            if element.get_attribute('title'):
                return True
            return False
