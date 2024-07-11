from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage


class ItemPage(BaseAppPage):
    ITEM_NAME = "//div[@class='product-details-inside_1UkX']//h1[@data-test-id='qa-pdp-name']"
    SIZE_OPTIONS_LOC = "//div[@data-test-id = 'qa-size-item']"
    COLOR_OPTIONS_LOC = "//div[@data-test-id= 'qa-color-item']"
    COLOR_TITLE_LOC = "span[class='label-dynamic_3Y3S']"
    PERCENTAGE_SALE_LOC = "//a[@class='tx-link-a stampa-sales_3ITt rtl_1_TU link_3vu6 tx-link_29YD']"
    FINAL_PRICE_LOC = "//div[@class='product-details-inside_1UkX']//div[@data-test-id='qa-pdp-price-final']"
    ACTUAL_PRICE_LOC = "div[class='row_2tcG strikethrough_t2Ab regular-price_35Lt']"
    ADD_TO_FAV_LIST_BUTTON_LOC = "//div[@class='product-details-inside_1UkX']//div[@class='wishlist_2WY2']/button"
    ITEM_TAG_LOC = "span[class='black-bg_2mJm']"
    BRAND_LOC = "//div[@class='right_1o65']/span"
    ITEM_NAME_LOC = "//div[@class='right_1o65']//a"
    QUICK_VIEW_LOC = "//div[@class='btn-quick_3Pv7 btn-quick-view_2SXw']"
    TAG_NAME_QUICK_VIEW_LOC = '//*[@id="panel-root"]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/span'
    BRAND_NAME_QUICK_VIEW_LOC = "a[class='tx-link-a brand_2ltz tx-link_29YD underline-hover_3GkV']"
    FINAL_PRICE_QUICK_VIEW_LOC = 'div[data-test-id="qa-pdp-price-final"]'
    SALE_PERCENT_QUICK_VIEW_LOC = 'a[class="tx-link-a stampa-sales_2O4Q link_3vu6 tx-link_29YD"]'
    ACTUAL_PRICE_QUICK_VIEW_LOC = '//div[@class="row_2tcG strikethrough_t2Ab prices-regular_yum0"]'
    TITLE_QUICK_VIEW_LOC = '//h1[@class="name_20R6"]'

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(self._driver, 10)
        self.item_name = wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEM_NAME)))
        self.final_price = wait.until(EC.element_to_be_clickable((By.XPATH, self.FINAL_PRICE_LOC)))
        self.color_options = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIZE_OPTIONS_LOC)))
        self.size_options = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIZE_OPTIONS_LOC)))
        self.add_to_fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_FAV_LIST_BUTTON_LOC)))

    def get_item_name(self):
        return self.item_name

    def get_final_price(self):
        return self.final_price

    def get_color_options(self):
        return self.color_options

    def get_size_options(self):
        return self.size_options

    def click_add_to_favorite_list(self):
        self.add_to_fav_button.click()

    def get_item_details(self):
        name = self.get_item_name().text()
        price = self.get_final_price().text()
        colors = self.get_color_options()
        colors[0].click()
        color = colors[0].text()
        sizes = self.get_size_options()
        sizes[0].click()
        size = sizes[0].text()
        item = Item(name, price, color, size)
        return item

