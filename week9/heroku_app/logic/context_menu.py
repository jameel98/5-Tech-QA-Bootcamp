from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from week9.heroku_app.infra.base_page import BasePage


class ContextMenu(BasePage):
    SPOT = "hot-spot"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/context_menu'

    def load(self):
        self._driver.get(self.url)

    def click_on_spot(self):
        context_menu_area = self._driver.find_element((By.ID, "hot-spot"))
        action_chains = ActionChains(self._driver)
        action_chains.context_click(context_menu_area).perform()

    def is_alert_displayed(self):
        # Wait for the alert to be present and switch to it
        return WebDriverWait(self._driver, 10).until(EC.alert_is_present())
