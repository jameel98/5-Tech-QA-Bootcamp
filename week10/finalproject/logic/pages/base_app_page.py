import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SEARCH_RESULTS_LOC = '//ol[@class="product-list_yyTm"]/li'

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def get_elements_list(self):
        """Retrieve the list of elements from the search results."""
        try:
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.SEARCH_RESULTS_LOC))
            )
            return self._driver.find_elements(By.XPATH, self.SEARCH_RESULTS_LOC)
        except Exception as e:
            self.logger.error(f"Failed to retrieve elements list: {e}")
            raise

    def get_search_results(self, search_title):
        """Check if search_title is present in any of the search results."""
        try:
            results = self.get_elements_list()

            for i in range(1, len(results) + 1):
                element = self._driver.find_element(By.XPATH, self.SEARCH_RESULTS_LOC + f"[{i}]/div[2]")
                title = element.get_attribute('title').lower()
                if search_title.lower() in title:
                    return True
            return False
        except Exception as e:
            self.logger.error(f"Failed to get search results for '{search_title}': {e}")
            raise

    def click_on_element(self):
        """Click on the first element in the search results."""
        try:
            items = self.get_elements_list()
            items[0].click()
        except Exception as e:
            self.logger.error(f"Failed to click on element: {e}")
            raise
