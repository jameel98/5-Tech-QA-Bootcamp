from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, driver):
        self.driver = driver

    def get_footer_text(self):
        return self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
