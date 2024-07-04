from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverSetup:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def get_driver(self):
        service = Service(self.driver_path)
        driver = webdriver.Chrome(service=service)
        return driver
