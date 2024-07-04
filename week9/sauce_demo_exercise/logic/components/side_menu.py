from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideMenu:
    MENU_BUTTON = 'react-burger-menu-btn'
    CLOSE_BUTTON = 'react-burger-cross-btn'
    LOGOUT = 'logout_sidebar_link'

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        menu_button = self.driver.find_element(By.ID, self.MENU_BUTTON)
        menu_button.click()

    def close_menu(self):
        close_button = self.driver.find_element(By.ID, self.CLOSE_BUTTON)
        close_button.click()

    def logout(self):
        self.open_menu()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.LOGOUT))
        )
        logout_link = self.driver.find_element(By.ID, self.LOGOUT)
        logout_link.click()
