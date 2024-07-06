from week9.heroku_app.infra.base_page import BasePage


class Slider(BasePage):

    SLIDE_INPUT = '//div[@class="sliderContainer"]/input'
    SLIDE_VAL = 'span[@id="range"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/horizontal_slider'

    def load(self):
        self._driver.get(self.url)

    def get_slider(self):
        return self.find_element(self.SLIDE_INPUT)

    def get_slide_value(self):
        return self.find_element(self.SLIDE_VAL)