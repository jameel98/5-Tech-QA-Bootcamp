from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class CartPage(BaseAppPage):
    CART_LIST_LOC = "//div[@class='cart-items-list_wmqo']"
    ITEM_CARD_LOC = "//div[@class='container_1XqK']"
    ITEM_NAME_LINK_LOC = "(//a[@class='tx-link-a name_1GBQ tx-link_29YD'])"

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_brand_locator(self, index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/strong/div'

    def get_item_link_locator(self, index):
        return f"(//a[@class='tx-link-a name_1GBQ tx-link_29YD'])[{index}]"

    def get_item_color_locator(self, index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[1]/span[@data-test-id="qa-item-color-value"]'

    def get_item_size_locator(self, index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[2]/span[@data-test-id="qa-item-size-value"]'

    def get_total_price_item_locator(self, index):
        return f'//div[@class="container_1XqK"][{index}]/div/div[@class="cart-item_3yl1 rtl_3YUG"]/div[@class="column_34Ze total-price_rLA-"]'

    def get_regular_price_item_locator(self, index):
        return f"(//div[@class='row_2tcG strikethrough_t2Ab price_kIgR'])[{index}]"

    def get_final_price_item_locator(self, index):
        return f"(//div[@class='row_2tcG bold_2wBM price-final_13zw'])[{index}]"

    def get_discount_item_locator(self, index):
        return f"(//a[@class='tx-link-a stampa-sales_3gHT link_3vu6 tx-link_29YD'])[{index}]"

    def get_quantity_item_locator(self, index):
        return f"(//div[@class='select-container_tSy-'])[{index}]"

    def get_delete_item_by_index_locator(self, index):
        return f"(//button[@class='tx-link-a icon_u36n remove_wqPe tx-link_29YD'])[{index}]"
