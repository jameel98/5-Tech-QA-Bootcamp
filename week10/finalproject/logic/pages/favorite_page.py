from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class FavoritePage(BaseAppPage):
    ITEMS_LIST_LOCATOR_LOC = "div[class='listing_2tNy']"
    ITEMS_CARD_LOC = "//li[@class='wishlist-product_2rk-']"
    ITEMS_NAME_LINK_LOC = "(//a[contains(@class,'tx-link-a title_3ZxJ')])"

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        self.items_list = wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEMS_LIST_LOCATOR_LOC)))
        self.cards = wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEMS_CARD_LOC)))
        self.names = wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEMS_NAME_LINK_LOC)))

    @staticmethod
    def get_item_brand_locator(index):
        return f'//li[{index}]//div[@class="right_1o65"]//span'

    @staticmethod
    def get_item_color_locator(index):
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"צבע")]'

    @staticmethod
    def get_item_size_locator(index):
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"מידה")]'

    @staticmethod
    def get_regular_price_item_locator(index):
        return f'//li[{index}]//div[@class="row_2tcG strikethrough_t2Ab regular-price_35Lt"]'

    @staticmethod
    def get_final_price_item_locator(index):
        return f'//li[{index}]//div[@class="row_2tcG bold_2wBM final-price_8CiX"]'

    @staticmethod
    def get_discount_item_locator(index):
        return f'//li[{index}]//a[@class="tx-link-a stampa-sales_3ITt rtl_1_TU link_3vu6 tx-link_29YD"]'

    def get_item_name(self, index):
        return self._driver.find_element(By.XPATH, self.names[index])

    def get_item_final_price(self, index):
        return self._driver.find_element(By.XPATH, self.get_final_price_item_locator(index))

    def get_item_size(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_size_locator(index))

    def get_item_color(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_color_locator(index))

    def get_item_details(self, index):
        name = self.get_item_name(index).text
        color = self.get_item_color(index).text
        size = self.get_item_size(index).text
        price = self.get_item_final_price(index).text

        item = Item(name, price, color, size)
        return item
