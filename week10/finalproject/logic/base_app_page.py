from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.parabank.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SIGNIN_BUTTON = '//div[text()="התחברות"]'
    AVATAR = '//span[@class="profile-button-new-menu-underline_1fv_"]'

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

    def get_search_input(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH)))

    def search_video(self, query):
        search_box = self.get_search_input()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def get_search_results(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.SEARCH_RESULTS))
        )
        results = self._driver.find_elements(By.CSS_SELECTOR, self.SEARCH_RESULTS)
        return [result.get_attribute('title') for result in results if result.get_attribute('title')]

    def click_on_first_video(self):
        # Wait for search results to load and click on the first video
        video_result = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.SEARCH_RESULTS))
        )
        video_result.click()

