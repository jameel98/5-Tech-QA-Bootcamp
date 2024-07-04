import unittest

from selenium.webdriver.common.by import By

from week9.sauce_demo_exercise.infra.web_driver import WebDriverSetup
from week9.sauce_demo_exercise.logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriverSetup().get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_standard(self):
        self.login_page.login_flow("standard_user", "secret_sauce")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_login_locked(self):
        self.login_page.login_flow('locked_out_user', 'secret_sauce')
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", error_message)

    def test_login_problem(self):
        self.login_page.login_flow('problem_user', 'secret_sauce')
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")
        # Additional checks for problem_user can be added here

    def test_login_performance_glitch(self):
        self.login_page.login_flow('performance_glitch_user', 'secret_sauce')
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")
        # Performance related assertions could be added here if needed

    def test_login_error_user(self):
        self.login_page.login_flow('error_user', 'secret_sauce')
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)

    def test_login_visual_user(self):
        self.login_page.login_flow('visual_user', 'secret_sauce')
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")
