from selenium.webdriver import ActionChains
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
    JUST_LANDED_LOC = "//a[text()='JUST LANDED']"
    ON_SALE_LOC = "//a[text()='ON SALE']"
    SPORTS_LOC = "//a[text()='SPORTS']"
    TRAIN_LOC = u"//a[text()='אימון']"

    def __init__(self, driver):
        self._driver = driver
        self.actions = ActionChains(self._driver)
        self.signin_button = self._driver.find_element(By.XPATH, self.SIGNIN_BUTTON_LOC)
        self.search_text_button = self._driver.find_element(By.XPATH, self.SEARCH_TEXT_BUTTON_LOC)
        self.fav_button = self._driver.find_element(By.XPATH, self.FAV_PAGE_BUTTON_LOC)
        self.cart_page_button = self._driver.find_element(By.XPATH, self.CART_PAGE_BUTTON_LOC)
        self.just_landed_button = self._driver.find_element(By.XPATH, self.JUST_LANDED_LOC)
        self.on_sale_button = self._driver.find_element(By.XPATH, self.ON_SALE_LOC)
        self.sports_button = self._driver.find_element(By.XPATH, self.SPORTS_LOC)

    def click_signin_button(self):
        self.signin_button.click()

    def click_search_text_button(self):
        self.search_text_button.click()

    def click_fav_page_button(self):
        self.fav_button.click()

    def click_cart_page_button(self):
        self.cart_page_button.click()

    def click_just_landed_button(self):
        self.just_landed_button.click()

    def click_on_sale_button(self):
        self.on_sale_button.click()

    def click_sports_button(self):
        self.sports_button.click()

    def hover_sports_button(self):
        self.actions.move_to_element(self.sports_button).perform()

    def click_train_button(self):
        wait = WebDriverWait(self._driver, 10)
        train = wait.until(EC.element_to_be_clickable((By.XPATH, self.TRAIN_LOC)))
        train.click()

    def get_avatar(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.AVATAR_LOC)))

    def get_search_text_input(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_INPUT_LOC)))
