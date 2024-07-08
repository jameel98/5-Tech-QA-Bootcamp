from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from week10.youtube.logic.base_app_page import BaseAppPage


class VideoPage(BaseAppPage):

    # //div[@id="title-wrapper"]/div[@id="menu"]
    SAVE_VIDEO = "//button[@aria-label='Save to playlist']"
    WATCH_LATER = "//yt-formatted-string[text()='Watch later']"
    MENU = '//div[@id="title-wrapper"]/div[@id="menu"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_save(self):
        save_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_VIDEO))
        )
        save_button.click()

    def select_watch_later(self):
        watch_later_option = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.WATCH_LATER))
        )
        watch_later_option.click()
