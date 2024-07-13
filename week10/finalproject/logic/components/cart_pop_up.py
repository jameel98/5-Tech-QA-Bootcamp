from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPopup:
    CART_BUTTON_LOC = "//div[@class='minicart-dropdown_2oUT']/div/div[@class='bottom_3LWp']/a"

    def __init__(self, driver):
        self._driver = driver

    def click_cart_button(self):
        wait = WebDriverWait(self._driver, 10)
        signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON_LOC)))
        signin_button.click()

