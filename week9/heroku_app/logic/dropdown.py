from week9.heroku_app.infra.base_page import BasePage


class DropDown(BasePage):
    DROPDOWN = "dropdown"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/dropdown'

    def load(self):
        self._driver.get(self.url)
