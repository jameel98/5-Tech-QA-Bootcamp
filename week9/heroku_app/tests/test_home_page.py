import unittest

from week9.heroku_app.infra.browser_wrapper import BrowserWrapper
from week9.heroku_app.infra.config_provider import ConfigProvider
from week9.heroku_app.logic.ab_page import ABPage
from week9.heroku_app.logic.add_remove_element import AddRemoveElement
from week9.heroku_app.logic.challenging_dom import ChallengingDom
from week9.heroku_app.logic.checkboxes import CheckBoxes
from week9.heroku_app.logic.home_page import HomePage


class TestInternet(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_home_page_links(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        self.assertEqual(len(links), 44)

    def test_A_B(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[0].click()

        self.ab_page = ABPage(self.driver)

        self.ab_page.load()
        self.assertEqual(self.ab_page.head_line().text, "A/B Test Control")

    def test_add_element(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[1].click()

        self.add_remove_page = AddRemoveElement(self.driver)
        self.add_remove_page.load()
        self.add_remove_page.add_element()
        elements_list = self.add_remove_page.get_elements_list()
        self.assertEqual(elements_list.size(), 1)

    def test_remove_element(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[1].click()

        self.add_remove_page = AddRemoveElement(self.driver)
        self.add_remove_page.load()
        self.add_remove_page.add_element()
        self.add_remove_page.get_elements_list()

        elements_list = self.add_remove_page.get_elements_list()
        elements_list[0].click()

        self.assertEqual(self.add_remove_page.get_elements_list().size(), 0)

    def test_challenging_dom_buttons(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[4].click()

        self.challenging_dom = ChallengingDom(self.driver)
        self.challenging_dom.load()

        # click buttons
        self.challenging_dom.click_button()
        self.challenging_dom.click_alert_button()
        self.challenging_dom.click_success_button()

    def test_check_boxes(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[5].click()

        self.check_boxes = CheckBoxes(self.driver)
        self.check_boxes.load()
        self.check_boxes.click_check_box1()
        self.check_boxes.click_check_box2()

