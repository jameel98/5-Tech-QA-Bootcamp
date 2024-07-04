import time
import unittest

from week9.ultimate_exercise_simple.infra.web_driver import WebDriverSetup
from week9.ultimate_exercise_simple.logic.ultimate_home_page import UltimatePage


class UltimatePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Arrange
        cls.driver_path = r'C:\Users\Admin\PycharmProjects\AI\automation project\chromedriver.exe'  # Update path
        cls.webdriver_setup = WebDriverSetup(cls.driver_path)
        cls.driver = cls.webdriver_setup.get_driver()
        cls.home_page = UltimatePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after a delay to see the results
        time.sleep(5)
        cls.driver.quit()

    def test_click_btn(self):
        self.home_page.load()
        self.home_page.click_btn(self.home_page.btn_click_me_loc)
        self.assertEqual(self.driver.current_url, "https://ultimateqa.com/?")

    def test_click_btn_id(self):
        self.home_page.load()
        self.home_page.click_btn(self.home_page.btn_id_loc)
        success_message = self.home_page.find_element(self.home_page.success_message_loc)
        self.assertIsNotNone(success_message)
        self.assertEqual(success_message, "Button success")

    def test_radio_btn(self):
        self.home_page.load()
        self.home_page.click_btn(self.home_page.radio_btn_loc)

        self.assertTrue(self.home_page.radio_btn_loc.is_selected())
    #
    #
    # def test_check_boxes(self):
    # def test_dropdown(self):
    # def test_table(self):
    # def test_table_no_id(self):
    #
