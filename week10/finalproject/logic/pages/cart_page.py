import logging
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
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class
        wait = WebDriverWait(self._driver, 10)
        self.names = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_NAME_LINK_LOC)))

    @staticmethod
    def get_item_color_locator(index):
        """Generate the XPath locator for the item's color based on its index."""
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[1]/span[@data-test-id="qa-item-color-value"]'

    @staticmethod
    def get_item_size_locator(index):
        """Generate the XPath locator for the item's size based on its index."""
        return f'//div[@class="container_1XqK"][{index}]/div/div[1]/div/div/div[2]/span[@data-test-id="qa-item-size-value"]'

    @staticmethod
    def get_final_price_item_locator(index):
        """Generate the XPath locator for the item's final price based on its index."""
        return f"(//div[@class='row_2tcG bold_2wBM price-final_13zw'])[{index}]"

    @staticmethod
    def get_delete_item_by_index_locator(index):
        """Generate the XPath locator for the delete item button based on its index."""
        return f"//div[@class='container_1XqK'][{index}]//button[@class='tx-link-a icon_u36n remove_wqPe tx-link_29YD']"

    def get_item_name(self, index):
        """Retrieve the name of the item based on its index."""
        return self.names[index - 1]

    def get_item_cards(self):
        """Retrieve all item cards from the cart list."""
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.ITEMS_CARD_LOC)))
        except Exception as e:
            self.logger.error(f"Failed to retrieve item cards: {e}")
            raise

    def empty_list_message(self):
        """Retrieve the message displayed when the cart is empty."""
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.visibility_of_element_located((By.XPATH, self.EMPTY_CART_MESSAGE_LOC)))
        except Exception as e:
            self.logger.error(f"Failed to retrieve empty list message: {e}")
            raise

    def get_item_final_price(self, index):
        """Retrieve the final price of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_final_price_item_locator(index))
        except Exception as e:
            self.logger.error(f"Failed to retrieve final price for item {index}: {e}")
            raise

    def get_item_size(self, index):
        """Retrieve the size of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_item_size_locator(index))
        except Exception as e:
            self.logger.error(f"Failed to retrieve size for item {index}: {e}")
            raise

    def get_item_color(self, index):
        """Retrieve the color of the item based on its index."""
        try:
            return self._driver.find_element(By.XPATH, self.get_item_color_locator(index))
        except Exception as e:
            self.logger.error(f"Failed to retrieve color for item {index}: {e}")
            raise

    def click_remove_button(self, index):
        """Click the remove button for the item based on its index."""
        try:
            remove_button = self._driver.find_element(By.XPATH, self.get_delete_item_by_index_locator(index))
            remove_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click remove button for item {index}: {e}")
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
            self.logger.error(f"Failed to retrieve details for item {index}: {e}")
            raise

    def remove_item(self, index):
        """Remove the item from the cart based on its index."""
        try:
            self.click_remove_button(index)
        except Exception as e:
            self.logger.error(f"Failed to remove item {index} from cart: {e}")
            raise
