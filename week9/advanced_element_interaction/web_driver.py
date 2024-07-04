from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverSetup:
    def __init__(self):
        self.driver_path = r"C:\Users\Admin\PycharmProjects\AI\automation project\chromedriver.exe"

    def get_driver(self):
        service = Service(self.driver_path)
        driver = webdriver.Chrome(service=service)
        return driver
