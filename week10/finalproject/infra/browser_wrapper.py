import json
from selenium import webdriver
import undetected_chromedriver as uc
from week10.parabank.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file('../config.json')
        print("Test Start")

    def get_driver(self, url):
        if self.config["browser"] == "Chrome":
            options = uc.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            self._driver = uc.Chrome(options=options)
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
