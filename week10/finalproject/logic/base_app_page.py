from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.components.navbar import NavBar
from week10.parabank.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SEARCH_RESULTS = '//ol[@class="product-list_yyTm"]/li'

    def __init__(self, driver):
        super().__init__(driver)
        self.navbar = NavBar(driver)

    def load(self):
        self._driver.get(self.get_config()["base_url"])

    def click_just_landed(self):
        self.navbar.click_just_landed_button()

    def click_on_sale(self):
        self.navbar.click_on_sale_button()

    def click_fav_list(self):
        self.navbar.click_fav_page_button()

    def click_cart_page_button(self):
        self.navbar.click_cart_page_button()

    def search_item_by_text(self, query):
        self.navbar.click_search_text_button()
        search_box = self.navbar.get_search_text_input()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def get_search_results(self, search_title):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_RESULTS))
        )
        results = self._driver.find_elements(By.XPATH, self.SEARCH_RESULTS)

        for i in range(1, len(results) + 1):
            element = self._driver.find_element(By.XPATH, self.SEARCH_RESULTS + f"[{i}]/div[2]")
            title = element.get_attribute('title').lower()
            print(title)
            print(search_title)
            if search_title.lower() in title:
                return True
            return False

    def find_elements_by_category_train(self):
        self.navbar.hover_sports_button()
        self.navbar.click_train_button()

