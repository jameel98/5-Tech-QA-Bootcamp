class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self._driver.reload()
