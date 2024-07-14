import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPopup:
    CART_BUTTON_LOC = "//div[@class='minicart-dropdown_2oUT']/div/div[@class='bottom_3LWp']/a"

    def __init__(self, driver):
        self._driver = driver
        self.logger = logging.getLogger(__name__)

    def click_cart_button(self):
        try:
            self.logger.info("Clicking on the cart button")
            wait = WebDriverWait(self._driver, 10)
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON_LOC)))
            cart_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click on cart button: {str(e)}")
            raise e
