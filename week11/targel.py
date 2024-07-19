from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from week10.finalproject.infra.browser_wrapper import BrowserWrapper
from selenium.webdriver.support import expected_conditions as EC


class Targel:
    SPORT_LOC = "//div[@class='mainNav']//a/span[text()=' ספורט']"

    def __init__(self):

        self._driver = webdriver.Chrome()

        self._driver.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")
        self._driver.maximize_window()

    def click_sport_button(self):
        wait = WebDriverWait(self._driver, 10)
        sport = wait.until(EC.element_to_be_clickable((By.XPATH, self.SPORT_LOC)))
        sport.click()

