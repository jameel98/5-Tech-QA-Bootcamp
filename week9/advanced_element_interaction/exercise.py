import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from week9.advanced_element_interaction.web_driver import WebDriverSetup


class TestDragAndDrop(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriverSetup().get_driver()
        # Set up the driver (ensure the path to your webdriver is correct)
        self.driver.get("https://www.solnet.co.il/klondike3")
        self.driver.maximize_window()

    def test_drag_and_drop(self):
        driver = self.driver
        # Find the elements to drag and drop (update selectors as necessary)
        source_element = driver.find_element(By.ID, 'card36')
        destination_element = driver.find_element(By.ID, 'card47')

        # Perform the drag and drop action
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, destination_element).perform()

    def tearDown(self):
        # Close the driver
        self.driver.quit()



    def spotcheck(self):
        # Find the table by its ID
        table = driver.find_element(By.ID, 'table1')

        # Get all rows in the table body
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        # Iterate through the rows and print the first name (first cell) of each row
        for row in rows:
            first_name = row.find_elements(By.TAG_NAME, 'td')[0].text
            print(first_name)


if __name__ == "__main__":
    unittest.main()
