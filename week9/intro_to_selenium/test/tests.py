import time
import unittest

from selenium.webdriver.common.by import By

from week9.intro_to_selenium.infra.web_driver import WebDriverSetup
from week9.intro_to_selenium.logic.googlepage import GoogleHomePage
from week9.intro_to_selenium.logic.searchpage import GoogleSearchResultsPage


class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Arrange
        cls.driver_path = r'C:\Users\Admin\PycharmProjects\AI\automation project\week9\intro_to_selenium\chromedriver.exe'  # Update path
        cls.webdriver_setup = WebDriverSetup(cls.driver_path)
        cls.driver = cls.webdriver_setup.get_driver()
        cls.home_page = GoogleHomePage(cls.driver)
        cls.results_page = GoogleSearchResultsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after a delay to see the results
        time.sleep(5)
        cls.driver.quit()

    def test_google_search(self):
        # Arrange
        search_query = 'Python programming'

        # Act
        self.home_page.load()
        self.home_page.enter_search_query(search_query)
        self.results_page.wait_for_results()

        # Assert
        results_div = self.driver.find_element(By.ID, self.results_page.results_div_id)
        self.assertIsNotNone(results_div)


if __name__ == '__main__':
    unittest.main()
