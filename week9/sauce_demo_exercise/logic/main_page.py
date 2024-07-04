from selenium.webdriver.common.by import By

from week9.sauce_demo_exercise.infra.base_page import BasePage


class MainPage(BasePage):
    HOME_HEADER_TEXT = '//div[@class="app_logo"]'
    SIDE_MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    SHOPPING_CART_BUTTON = '//div[@id="shopping_cart_container"]'
    BACK_PACK = 'backpack'
    BIKE_LIGHTS = 'bike-light'
    BOLT_T_SHIRT = 'bolt-t-shirt'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

        self._home_header_text = self._driver.find_element(By.XPATH, self.HOME_HEADER_TEXT)
        self._side_menu_button = self._driver.find_element(By.XPATH, self.SIDE_MENU_BUTTON)
        self._shopping_cart_button = self._driver.find_element(By.XPATH, self.SHOPPING_CART_BUTTON)

    def load(self):
        self._driver.get(self.url)

    def is_header_displayed(self):
        if self._home_header_text:
            return True
        return False

    def click_side_menu_button(self):
        self._side_menu_button.click()

    def click_cart_button(self):
        self._shopping_cart_button.click()

    def add_item_to_cart(self, item_name):
        item = self._driver.find_element(By.XPATH, f"//button[@id='add-to-cart-sauce-labs-{item_name}']")
        item.click()

    def remove_item_from_cart(self, item_name):
        item = self._driver.find_element(By.XPATH, f"//button[@id='remove-sauce-labs-{item_name}']")
        item.click()

