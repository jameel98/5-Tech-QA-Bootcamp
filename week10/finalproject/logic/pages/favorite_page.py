from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class FavoritePage(BaseAppPage):
    ITEMS_CARD_LOC = "//li[@class='wishlist-product_2rk-']"
    ITEMS_NAME_LINK_LOC = "(//a[contains(@class,'tx-link-a title_3ZxJ')])"
    EDIT_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    REMOVE_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    EMPTY_LIST_MESSAGE_LOC = "//div[@class='warning_1vFK toast_hN0l rtl_1l4_ showing_1n_C no-items_3PJg']/span"

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        self.names = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_NAME_LINK_LOC)))

    @staticmethod
    def get_item_color_locator(index):
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"צבע")]'

    @staticmethod
    def get_item_size_locator(index):
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"מידה")]'

    @staticmethod
    def get_final_price_item_locator(index):
        return f'//li[{index}]//div[@class="row_2tcG bold_2wBM final-price_8CiX"]'

    @staticmethod
    def get_item_remove_button_locator(index):
        return f"//div[@class='btn-ltr_35WF btn-quick_3Pv7 btn-remove_274T'][{index}]"

    def get_item_name(self, index):
        return self.names[index - 1]

    def click_edit_button(self, index):
        wait = WebDriverWait(self._driver, 10)
        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.EDIT_ITEM_BUTTON_LOC + f"{index}")))
        edit_button.click()

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
        price = self.get_item_final_price(index).text

        item = Item(name, price, color)
        return item

    def remove_item(self, index):
        self.click_remove_button(index)
