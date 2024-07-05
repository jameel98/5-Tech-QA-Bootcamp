

from week9.heroku_app.infra.base_page import BasePage


class DragDrop(BasePage):
    A = "column-a"
    B = "column-b"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/drag_and_drop'

    def load(self):
        self._driver.get(self.url)

