import os
import time
import logging

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.infra.base_page import BasePage

class NavBar(BasePage):
    SIGNIN_BUTTON_LOC = '//button[@data-test-id="qa-header-login-button"]'
    AVATAR_LOC = '//span[@class="profile-button-new-menu-underline_1fv_"]'
    SEARCH_TEXT_BUTTON_LOC = '//div[@id="app-root"]//button[@class="search-button_1ENs"]'
    SEARCH_TEXT_INPUT_LOC = '//input[@class="input_sILM"]'
    FAV_PAGE_BUTTON_LOC = "//a[@data-test-id='qa-link-wishlist']"
    CART_PAGE_BUTTON_LOC = "//a[@data-test-id='qa-link-minicart']"
    OVERLAY_LOC = "//div[@class='fullscreen-overlay_2pj0']"

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(self._driver)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def click_signin_button(self):
        """Clicks on the sign-in button in the navigation bar."""
        try:
            wait = WebDriverWait(self._driver, 20)
            signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON_LOC)))
            signin_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click sign-in button: {e}")
            raise

    def click_fav_page_button(self):
        """Clicks on the favorite page button in the navigation bar."""
        try:
            wait = WebDriverWait(self._driver, 20)
            fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.FAV_PAGE_BUTTON_LOC)))
            fav_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click favorite page button: {e}")
            raise

    def click_cart_page_button(self):
        """Clicks on the cart page button in the navigation bar."""
        try:
            wait = WebDriverWait(self._driver, 20)
            cart_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_PAGE_BUTTON_LOC)))
            cart_page_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click cart page button: {e}")
            raise

    def click_search_text_button(self):
        """Clicks on the search text button in the navigation bar."""
        try:
            WebDriverWait(self._driver, 20).until(EC.invisibility_of_element_located((By.XPATH, self.OVERLAY_LOC)))

            wait = WebDriverWait(self._driver, 20)
            search_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_BUTTON_LOC)))
            search_text_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click search text button: {e}")
            raise

    def hover_over_outer_category(self, category):
        """Performs a hover action over an outer category link."""
        try:
            wait = WebDriverWait(self._driver, 20)
            category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
            self.actions.move_to_element(category_btn).perform()
        except Exception as e:
            self.logger.error(f"Failed to hover over outer category '{category}': {e}")
            raise

    def click_on_outer_category(self, category):
        """Clicks on an outer category link."""
        try:
            wait = WebDriverWait(self._driver, 20)
            category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
            category_btn.click()
        except Exception as e:
            self.logger.error(f"Failed to click on outer category '{category}': {e}")
            raise

    def click_on_inner_category(self, category):
        """Clicks on an inner category link."""
        try:
            wait = WebDriverWait(self._driver, 20)
            inner_category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
            inner_category_btn.click()
        except Exception as e:
            self.logger.error(f"Failed to click on inner category '{category}': {e}")
            raise

    def get_avatar(self):
        """Returns the avatar element."""
        try:
            wait = WebDriverWait(self._driver, 20)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.AVATAR_LOC)))
        except Exception as e:
            self.logger.error(f"Failed to get avatar: {e}")
            raise

    def get_search_text_input(self):
        """Returns the search text input element."""
        try:
            wait = WebDriverWait(self._driver, 20)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_INPUT_LOC)))
        except Exception as e:
            self.logger.error(f"Failed to get search text input: {e}")
            raise

    def search_item_by_text_flow(self, query):
        """Performs a search flow by entering a query into the search text input."""
        try:
            self.click_search_text_button()
            search_box = self.get_search_text_input()
            search_box.send_keys(query)
            search_box.send_keys(Keys.ENTER)
        except Exception as e:
            self.logger.error(f"Failed to perform search for '{query}': {e}")
            raise
