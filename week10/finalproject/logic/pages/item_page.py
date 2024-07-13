from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class ItemPage(BaseAppPage):
    ITEM_NAME = "//div[@class='product-details-inside_1UkX']//h1[@data-test-id='qa-pdp-name']"
    SIZE_OPTIONS_LOC = "//div[@class='product-attributes-wrapper_3Ro3']//div[@data-test-id = 'qa-size-item']"
    COLOR_OPTIONS_LOC = "//div[@class='info-column_3TEX']//div[@data-test-id= 'qa-color-item']"
    COLOR_TITLE_LOC = "span[class='label-dynamic_3Y3S']"
    PERCENTAGE_SALE_LOC = "//a[@class='tx-link-a stampa-sales_3ITt rtl_1_TU link_3vu6 tx-link_29YD']"
    FINAL_PRICE_LOC = "//div[@class='product-details-inside_1UkX']//div[@data-test-id='qa-pdp-price-final']"
    ACTUAL_PRICE_LOC = "div[class='row_2tcG strikethrough_t2Ab regular-price_35Lt']"
    ADD_TO_FAV_LIST_BUTTON_LOC = "//div[@class='product-details-inside_1UkX']//div[@class='wishlist_2WY2']/button"
    ADD_TO_CART_LIST_BUTTON_LOC = "//button[@data-test-id='qa-add-to-cart-button']"
    ITEM_TAG_LOC = "span[class='black-bg_2mJm']"
    BRAND_LOC = "//div[@class='right_1o65']/span"
    ITEM_NAME_LOC = "//div[@class='right_1o65']//a"
    MISSING_SIZE_ERROR_LOC = "//span[text()='מידה - שדה חובה.']"
    MISSING_COLOR_ERROR_LOC = "//span[text()='שדה חובה.']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_name(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEM_NAME)))

    def get_final_price(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.FINAL_PRICE_LOC)))

    def get_color_options(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.COLOR_OPTIONS_LOC)))

    def get_size_options(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.SIZE_OPTIONS_LOC)))

    def click_add_to_favorite_list(self):
        wait = WebDriverWait(self._driver, 10)
        add_to_fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_FAV_LIST_BUTTON_LOC)))
        add_to_fav_button.click()

    def click_add_to_cart_list(self):
        wait = WebDriverWait(self._driver, 10)
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_LIST_BUTTON_LOC)))
        add_to_cart_button.click()

    def get_size_error_message(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.MISSING_SIZE_ERROR_LOC)))

    def get_color_error_message(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.MISSING_COLOR_ERROR_LOC)))

    def remove_color(self):
        colors = self.get_color_options()
        if 'selected' in colors[0].get_attribute('class'):
            colors[0].click()
        else:
            colors[0].click()
            colors[0].click()

    def pick_color(self):
        colors = self.get_color_options()
        if 'selected' in colors[0].get_attribute('class'):
            return colors[0].get_attribute('title')
        else:
            colors[0].click()
            return colors[0].get_attribute('title')

    def remove_size(self):
        sizes = self.get_size_options()
        if 'selected' in sizes[0].get_attribute('class'):
            sizes[0].click()
        else:
            sizes[0].click()
            sizes[0].click()

    def pick_size(self):
        sizes = self.get_size_options()
        if 'selected' in sizes[0].get_attribute('class'):
            return sizes[0].text
        else:
            sizes[0].click()
            return sizes[0].text

    def get_item_details(self):
        name = self.get_item_name().text
        price = self.get_final_price().text
        color = self.pick_color()
        size = self.pick_size()
        item = Item(name, price, color, size)
        return item

    def get_item_details_no_size(self):
        name = self.get_item_name().text
        price = self.get_final_price().text
        color = self.pick_color()
        self.remove_size()
        item = Item(name, price, color, "")
        return item

    def get_item_details_no_color(self):
        name = self.get_item_name().text
        price = self.get_final_price().text
        self.remove_color()
        size = self.pick_size()
        item = Item(name, price, "", size)
        return item
