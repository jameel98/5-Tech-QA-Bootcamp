from selenium import webdriver

from week10.parabank.infra.config_provider import ConfigProvider


class BasePage:

    # Always get driver
    def __init__(self, driver: webdriver):
        self._driver = driver
        self.config = ConfigProvider.load_from_file('../config.json')
        self.url = self.config["base_url"]

    def load(self):
        self._driver.get(self.url)

    def refresh_page(self):
        self._driver.refresh()

    def get_config(self):
        return self.config
