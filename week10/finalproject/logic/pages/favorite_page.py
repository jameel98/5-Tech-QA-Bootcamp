from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class FavoritePage(BaseAppPage):
    # ITEMS_LIST_LOCATOR_LOC = "div[class='listing_2tNy']"
    ITEMS_CARD_LOC = "//li[@class='wishlist-product_2rk-']"
    ITEMS_NAME_LINK_LOC = "(//a[contains(@class,'tx-link-a title_3ZxJ')])"
    EDIT_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    REMOVE_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    EMPTY_LIST_MESSAGE_LOC = "//div[@class='warning_1vFK toast_hN0l rtl_1l4_ showing_1n_C no-items_3PJg']/span"

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        # self.items_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_LIST_LOCATOR_LOC)))
        self.names = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_NAME_LINK_LOC)))

    def click_edit_button(self, index):
        wait = WebDriverWait(self._driver, 10)
        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.EDIT_ITEM_BUTTON_LOC + f"{index}")))
        edit_button.click()

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

    @staticmethod
    def get_item_remove_button_locator(index):
        return f"//div[@class='btn-ltr_35WF btn-quick_3Pv7 btn-remove_274T'][{index}]"

    def get_item_name(self, index):
        return self.names[index - 1]

    def get_item_cards(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_CARD_LOC)))

    def empty_list_message(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.EMPTY_LIST_MESSAGE_LOC)))

    def get_item_final_price(self, index):
        return self._driver.find_element(By.XPATH, self.get_final_price_item_locator(index))

    def get_item_size(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_size_locator(index))

    def get_item_color(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_color_locator(index))

    def click_remove_button(self, index):
        remove_button = self._driver.find_element(By.XPATH, self.get_item_remove_button_locator(index))
        remove_button.click()

    def get_item_details(self, index):
        name = self.get_item_name(index).text
        color = self.get_item_color(index).text
        # size = self.get_item_size(index).text  size doesnt appear
        price = self.get_item_final_price(index).text

        item = Item(name, price, color, f"41 1\3")
        return item

    def remove_item(self, index):
        self.click_remove_button(index)
