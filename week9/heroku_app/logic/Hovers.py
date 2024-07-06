from week9.heroku_app.infra.base_page import BasePage


class Hovers(BasePage):

    AVATAR = '//div[@class="figure"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://the-internet.herokuapp.com/hovers'

    def load(self):
        self._driver.get(self.url)

    def get_avatar(self, num):
        return self.find_element(self.AVATAR + f"{num}")

    def get_user_name(self, num):
        return self.find_element(f"//div[@class='figure'][{num}]/div[@class='figcaption']/h5")