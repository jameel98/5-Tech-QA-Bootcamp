from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class CartPage(BaseAppPage):
    CART_LIST_LOC = "//div[@class='cart-items-list_wmqo']"
    ITEMS_CARD_LOC = "//div[@class='container_1XqK']"
    ITEMS_NAME_LINK_LOC = "(//a[@class='tx-link-a name_1GBQ tx-link_29YD'])"
    REMOVE_ITEM_LOC = "//div[@class='container_1XqK'][1]//button[@class='tx-link-a icon_u36n remove_wqPe tx-link_29YD']"
    EMPTY_CART_MESSAGE_LOC = "//div[@class='cart-empty_2gU9']/p"

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        self.names = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_NAME_LINK_LOC)))

    @staticmethod
    def get_item_brand_locator(index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/strong/div'

    @staticmethod
    def get_item_link_locator(index):
        return f"(//a[@class='tx-link-a name_1GBQ tx-link_29YD'])[{index}]"

    @staticmethod
    def get_item_color_locator(index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[1]/span[@data-test-id="qa-item-color-value"]'

    @staticmethod
    def get_item_size_locator(index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[2]/span[@data-test-id="qa-item-size-value"]'

    @staticmethod
    def get_total_price_item_locator(index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[@class="cart-item_3yl1 rtl_3YUG"]/div[@class="column_34Ze total-price_rLA-"]'

    @staticmethod
    def get_regular_price_item_locator(index):
        return f"(//div[@class='row_2tcG strikethrough_t2Ab price_kIgR'])[{index}]"

    @staticmethod
    def get_final_price_item_locator( index):
        return f"(//div[@class='row_2tcG bold_2wBM price-final_13zw'])[{index}]"

    @staticmethod
    def get_discount_item_locator( index):
        return f"(//a[@class='tx-link-a stampa-sales_3gHT link_3vu6 tx-link_29YD'])[{index}]"

    @staticmethod
    def get_quantity_item_locator( index):
        return f"(//div[@class='select-container_tSy-'])[{index}]"

    @staticmethod
    def get_delete_item_by_index_locator( index):
        return f"//div[@class='container_1XqK'][{index}]//button[@class='tx-link-a icon_u36n remove_wqPe tx-link_29YD']"

    def get_item_name(self, index):
        return self.names[index - 1]

    def get_item_cards(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_CARD_LOC)))

    def empty_list_message(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.EMPTY_CART_MESSAGE_LOC)))

    def get_item_final_price(self, index):
        return self._driver.find_element(By.XPATH, self.get_final_price_item_locator(index))

    def get_item_size(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_size_locator(index))

    def get_item_color(self, index):
        return self._driver.find_element(By.XPATH, self.get_item_color_locator(index))

    def click_remove_button(self, index):
        remove_button = self._driver.find_element(By.XPATH, self.get_delete_item_by_index_locator(index))
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

