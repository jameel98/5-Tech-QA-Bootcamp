from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.results_div_id = 'search'

    def wait_for_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.results_div_id))
        )
