from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.infra.logger_setup import LogSetup  # Import the LogSetup class


class FavoritePage(BaseAppPage):
    ITEMS_CARD_LOC = "//li[@class='wishlist-product_2rk-']"
    ITEMS_NAME_LINK_LOC = "(//a[contains(@class,'tx-link-a title_3ZxJ')])"
    EDIT_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    REMOVE_ITEM_BUTTON_LOC = "//div[@class='btn-quick_3Pv7 btn-edit_252-']"
    EMPTY_LIST_MESSAGE_LOC = "//div[@class='warning_1vFK toast_hN0l rtl_1l4_ showing_1n_C no-items_3PJg']/span"

    def __init__(self, driver):
        super().__init__(driver)
        log_setup = LogSetup()
        self.logger = log_setup.logger
        try:
            wait = WebDriverWait(self._driver, 10)
            self.names = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_NAME_LINK_LOC)))
        except Exception as e:
            self.logger.error(f"Error initializing FavoritePage: {e}")
            raise

    @staticmethod
    def get_item_color_locator(index):
        """Generate the XPATH locator for the item's color based on its index."""
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"צבע")]'

    @staticmethod
    def get_item_size_locator(index):
        """Generate the XPATH locator for the item's size based on its index."""
        return f'(//div[@class="wrap_3QMJ rtl_2lAP"])[{index}]//span[contains(text(),"מידה")]'

    @staticmethod
    def get_final_price_item_locator(index):
        """Generate the XPATH locator for the item's final price based on its index."""
        return f'//li[{index}]//div[@class="row_2tcG bold_2wBM final-price_8CiX"]'

    @staticmethod
    def get_item_remove_button_locator(index):
        """Generate the XPATH locator for the item's remove button based on its index."""
        return f"//div[@class='btn-ltr_35WF btn-quick_3Pv7 btn-remove_274T'][{index}]"

    def get_item_name(self, index):
        """Retrieve the name of the item based on its index."""
        try:
            return self.names[index - 1]
        except Exception as e:
            self.logger.error(f"Error getting item name for index {index}: {e}")
            raise

    def click_edit_button(self, index):
        """Click the edit button for the item based on its index."""
        try:
            wait = WebDriverWait(self._driver, 10)
            edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.EDIT_ITEM_BUTTON_LOC + f"{index}")))
            edit_button.click()
            self.logger.info(f"Clicked edit button for index {index}.")
        except Exception as e:
            self.logger.error(f"Error clicking edit button for index {index}: {e}")
            raise

    def get_item_cards(self):
        """Retrieve all item cards from the favorite list."""
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_CARD_LOC)))
        except Exception as e:
            self.logger.error("Error getting item cards: {e}")
            raise

    def empty_list_message(self):
        """Retrieve the message displayed when the favorite list is empty."""
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.visibility_of_element_located((By.XPATH, self.EMPTY_LIST_MESSAGE_LOC)))
        except Exception as e:
            self.logger.error("Error getting empty list message: {e}")
            raise

    def get_item_final_price(self, index):
        """Retrieve the final price of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_final_price_item_locator(index))
        except Exception as e:
            self.logger.error(f"Error getting final price for item at index {index}: {e}")
            raise

    def get_item_size(self, index):
        """Retrieve the size of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_item_size_locator(index))
        except Exception as e:
            self.logger.error(f"Error getting size for item at index {index}: {e}")
            raise

    def get_item_color(self, index):
        """Retrieve the color of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_item_color_locator(index))
        except Exception as e:
            self.logger.error(f"Error getting color for item at index {index}: {e}")
            raise

    def click_remove_button(self, index):
        """Click the remove button for the item based on its index."""
        try:
            remove_button = self._driver.find_element(By.XPATH, self.get_item_remove_button_locator(index))
            remove_button.click()
        except Exception as e:
            self.logger.error(f"Error clicking remove button for item at index {index}: {e}")
            raise

    def get_item_details(self, index):
        """Get the details of the item including name, price, and color based on its index."""
        try:
            name = self.get_item_name(index).text
            color = self.get_item_color(index).text
            price = self.get_item_final_price(index).text
            item = Item(name, price, color)
            return item
        except Exception as e:
            self.logger.error(f"Error getting item details for index {index}: {e}")
            raise

    def remove_item(self, index):
        """Remove the item from the favorite list based on its index."""
        try:
            self.click_remove_button(index)
        except Exception as e:
            self.logger.error(f"Error removing item at index {index}: {e}")
            raise
