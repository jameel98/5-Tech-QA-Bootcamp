from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavBar:
    SIGNIN_BUTTON_LOC = '//button[@data-test-id="qa-header-login-button"]'
    AVATAR_LOC = '//span[@class="profile-button-new-menu-underline_1fv_"]'
    SEARCH_TEXT_BUTTON_LOC = '//button[@class="search-button_1ENs"]'
    SEARCH_TEXT_INPUT_LOC = '//input[@class="input_sILM"]'
    FAV_PAGE_BUTTON_LOC = "//a[@data-test-id='qa-link-wishlist']"
    CART_PAGE_BUTTON_LOC = "//a[@data-test-id='qa-link-minicart']"
    OVERLAY_LOC = "//div[@class='fullscreen-overlay_2pj0']"

    def __init__(self, driver):
        self._driver = driver
        self.actions = ActionChains(self._driver)
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.OVERLAY_LOC)))

        wait = WebDriverWait(self._driver, 10)
        self.signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON_LOC)))
        self.search_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_BUTTON_LOC)))
        self.fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.FAV_PAGE_BUTTON_LOC)))
        self.cart_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_PAGE_BUTTON_LOC)))

    def click_signin_button(self):
        self.signin_button.click()

    def click_fav_page_button(self):
        self.fav_button.click()

    def click_cart_page_button(self):
        self.cart_page_button.click()

    def click_search_text_button(self):
        self.search_text_button.click()

    def hover_over_outer_category(self, category):
        wait = WebDriverWait(self._driver, 10)
        category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
        self.actions.move_to_element(category_btn).perform()

    def click_on_outer_category(self, category):
        wait = WebDriverWait(self._driver, 10)
        category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
        category_btn.click()

    def click_on_inner_category(self, category):
        wait = WebDriverWait(self._driver, 10)
        train = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']")))
        train.click()

    def get_avatar(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.AVATAR_LOC)))

    def get_search_text_input(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_INPUT_LOC)))

    def search_item_by_text_flow(self, query):
        self.click_search_text_button()
        search_box = self.get_search_text_input()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

