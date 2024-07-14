from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.finalproject.logic.objects.item import Item
from week10.finalproject.logic.pages.base_app_page import BaseAppPage
from week10.finalproject.infra.logger_setup import LogSetup


class ItemPage(BaseAppPage):
    ITEM_NAME = "//div[@class='product-details-inside_1UkX']//h1[@data-test-id='qa-pdp-name']"
    SIZE_OPTIONS_LOC = "//div[@class='product-attributes-wrapper_3Ro3']//div[@data-test-id = 'qa-size-item']"
    COLOR_OPTIONS_LOC = "//div[@class='info-column_3TEX']//div[@data-test-id= 'qa-color-item']"
    COLOR_TITLE_LOC = "span[class='label-dynamic_3Y3S']"
    FINAL_PRICE_LOC = "//div[@class='product-details-inside_1UkX']//div[@data-test-id='qa-pdp-price-final']"
    ADD_TO_FAV_LIST_BUTTON_LOC = "//div[@class='product-details-inside_1UkX']//div[@class='wishlist_2WY2']/button"
    ADD_TO_CART_LIST_BUTTON_LOC = "//button[@data-test-id='qa-add-to-cart-button']"
    MISSING_SIZE_ERROR_LOC = "//span[text()='מידה - שדה חובה.']"
    MISSING_COLOR_ERROR_LOC = "//span[text()='שדה חובה.']"

    def __init__(self, driver):
        super().__init__(driver)
        log_setup = LogSetup()
        self.logger = log_setup.logger

    def get_item_name(self):
        """Retrieve the item's name from the web page."""
        try:
            self.logger.info("Waiting for item name to be clickable.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.ITEM_NAME)))
        except Exception as e:
            self.logger.error(f"Error getting item name: {e}")
            raise

    def get_final_price(self):
        """Retrieve the final price of the item from the web page."""
        try:
            self.logger.info("Waiting for final price to be clickable.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.FINAL_PRICE_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting final price: {e}")
            raise

    def get_color_options(self):
        """Retrieve the color options for the item."""
        try:
            self.logger.info("Waiting for color options to be present.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.COLOR_OPTIONS_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting color options: {e}")
            raise

    def get_size_options(self):
        """Retrieve the size options for the item."""
        try:
            self.logger.info("Waiting for size options to be present.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.SIZE_OPTIONS_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting size options: {e}")
            raise

    def click_add_to_favorite_list(self):
        """Click the button to add the item to the favorite list."""
        try:
            self.logger.info("Waiting for add to favorite list button to be clickable.")
            wait = WebDriverWait(self._driver, 10)
            add_to_fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_FAV_LIST_BUTTON_LOC)))
            add_to_fav_button.click()
            self.logger.info("Clicked add to favorite list button.")
        except Exception as e:
            self.logger.error(f"Error clicking add to favorite list button: {e}")
            raise

    def click_add_to_cart_list(self):
        """Click the button to add the item to the cart."""
        try:
            self.logger.info("Waiting for add to cart list button to be clickable.")
            wait = WebDriverWait(self._driver, 10)
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_LIST_BUTTON_LOC)))
            add_to_cart_button.click()
            self.logger.info("Clicked add to cart list button.")
        except Exception as e:
            self.logger.error(f"Error clicking add to cart list button: {e}")
            raise

    def get_size_error_message(self):
        """Retrieve the error message displayed when size is not selected."""
        try:
            self.logger.info("Waiting for size error message to be visible.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.MISSING_SIZE_ERROR_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting size error message: {e}")
            raise

    def get_color_error_message(self):
        """Retrieve the error message displayed when color is not selected."""
        try:
            self.logger.info("Waiting for color error message to be visible.")
            wait = WebDriverWait(self._driver, 10)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.MISSING_COLOR_ERROR_LOC)))
        except Exception as e:
            self.logger.error(f"Error getting color error message: {e}")
            raise

    def remove_color(self):
        """Remove the selected color."""
        try:
            self.logger.info("Removing selected color.")
            colors = self.get_color_options()
            if 'selected' in colors[0].get_attribute('class'):
                colors[0].click()
            else:
                colors[0].click()
                colors[0].click()
        except Exception as e:
            self.logger.error(f"Error removing color: {e}")
            raise

    def pick_color(self):
        """Pick a color for the item."""
        try:
            self.logger.info("Picking a color.")
            colors = self.get_color_options()
            if 'selected' in colors[0].get_attribute('class'):
                return colors[0].get_attribute('title')
            else:
                colors[0].click()
                return colors[0].get_attribute('title')
        except Exception as e:
            self.logger.error(f"Error picking color: {e}")
            raise

    def remove_size(self):
        """Remove the selected size."""
        try:
            self.logger.info("Removing selected size.")
            sizes = self.get_size_options()
            if 'selected' in sizes[0].get_attribute('class'):
                sizes[0].click()
            else:
                sizes[0].click()
                sizes[0].click()
        except Exception as e:
            self.logger.error(f"Error removing size: {e}")
            raise

    def pick_size(self):
        """Pick a size for the item."""
        try:
            self.logger.info("Picking a size.")
            sizes = self.get_size_options()
            if 'selected' in sizes[0].get_attribute('class'):
                return sizes[0].text
            else:
                sizes[0].click()
                return sizes[0].text
        except Exception as e:
            self.logger.error(f"Error picking size: {e}")
            raise

    def get_item_details(self):
        """Get the details of the item including name, price, color, and size."""
        try:
            self.logger.info("Getting item details.")
            name = self.get_item_name().text
            price = self.get_final_price().text
            color = self.pick_color()
            size = self.pick_size()
            item = Item(name, price, color)
            self.logger.info(f"Item details: Name={name}, Price={price}, Color={color}, Size={size}")
            return item
        except Exception as e:
            self.logger.error(f"Error getting item details: {e}")
            raise

    def get_item_details_no_size(self):
        """Get the details of the item excluding size."""
        try:
            self.logger.info("Getting item details without size.")
            name = self.get_item_name().text
            price = self.get_final_price().text
            color = self.pick_color()
            self.remove_size()
            item = Item(name, price, color)
            self.logger.info(f"Item details without size: Name={name}, Price={price}, Color={color}")
            return item
        except Exception as e:
            self.logger.error(f"Error getting item details without size: {e}")
            raise

    def get_item_details_no_color(self):
        """Get the details of the item excluding color."""
        try:
            self.logger.info("Getting item details without color.")
            name = self.get_item_name().text
            price = self.get_final_price().text
            self.remove_color()
            size = self.pick_size()
            item = Item(name, price, "")
            self.logger.info(f"Item details without color: Name={name}, Price={price}, Size={size}")
            return item
        except Exception as e:
            self.logger.error(f"Error getting item details without color: {e}")
            raise
