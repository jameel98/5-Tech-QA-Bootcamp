from week9.sauce_demo_exercise.logic.components.footer import Footer
from week9.sauce_demo_exercise.logic.components.header import Header
from week9.sauce_demo_exercise.logic.components.side_menu import SideMenu


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.driver = driver
        self.header = Header(driver)
        self.footer = Footer(driver)
        self.side_menu = SideMenu(driver)

    def refresh_page(self):
        self._driver.reload()
