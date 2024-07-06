from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week9.heroku_app.infra.base_page import BasePage


class GeoLocation(BasePage):

    BUTTON = '//button'
    LAT = 'div//[@id="lat-value"]'
    LONG = 'div//[@id="long-value"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/geolocation'

    def load(self):
        self._driver.get(self.url)

    def click_location(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON))
        )
        button.click()

    def is_location_displayed(self):
        lat = self._driver.find_element(By.XPATH, self.LAT).isDisplayed()
        long = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LONG))
        )

        return lat.isDisplayed() and long.isDisplayed()
