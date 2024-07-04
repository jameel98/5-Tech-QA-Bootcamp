import time
import unittest

from week9.ultimate_exercise_complicated.infra.web_driver import WebDriverSetup
from week9.ultimate_exercise_complicated.logic.ultimate_home_page import UltimatePage


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

    def test_all_btns(self):
        self.home_page.load()
        for i in range(0, 12):
            self.home_page.click_btn(f"//a [@class=\"et_pb_button et_pb_button_{i} et_pb_bg_layout_light\"]")
            self.driver.implicitly_wait(2000)

