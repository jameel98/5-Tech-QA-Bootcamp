from selenium.webdriver.common.by import By

from week9.sauce_demo_exercise.infra.base_page import BasePage


class ShoppingCartPage(BasePage):

    ITEM = 'cart_item'

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, self.ITEM)
        return items

    def remove_item_from_cart(self, item_name):
        item = self._driver.find_element(By.XPATH, f"//button[@id='remove-sauce-labs-{item_name}']")
        item.click()

