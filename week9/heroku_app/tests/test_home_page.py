import os
import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from week9.heroku_app.infra.browser_wrapper import BrowserWrapper
from week9.heroku_app.infra.config_provider import ConfigProvider
from week9.heroku_app.logic.ab_page import ABPage
from week9.heroku_app.logic.add_remove_element import AddRemoveElement
from week9.heroku_app.logic.challenging_dom import ChallengingDom
from week9.heroku_app.logic.checkboxes import CheckBoxes
from week9.heroku_app.logic.context_menu import ContextMenu
from week9.heroku_app.logic.drag_drop import DragDrop
from week9.heroku_app.logic.dropdown import DropDown
from week9.heroku_app.logic.dynamic_controls import DynamicControls
from week9.heroku_app.logic.file_download import FileDownload
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

    def test_challenging_dom_table(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[4].click()

        self.challenging_dom = ChallengingDom(self.driver)
        self.challenging_dom.load()

        table_headers = self.challenging_dom.get_table_header()
        table_body = self.challenging_dom.get_table_body()

        header_texts = [header.text for header in table_headers]
        print("Table headers:", header_texts)

        for row in table_body:
            cells = row.find_elements(By.TAG_NAME, "td")
            cell_texts = [cell.text for cell in cells]
            print("Table row:", cell_texts)

    def test_challenging_dom_canvas(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[4].click()

        self.challenging_dom = ChallengingDom(self.driver)
        self.challenging_dom.load()
        self.challenging_dom.canvas()

    def test_click_check_boxes(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[5].click()

        self.check_boxes = CheckBoxes(self.driver)
        self.check_boxes.load()
        self.check_boxes.click_check_box1()

    def test_unclick_check_boxes(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[5].click()

        self.check_boxes = CheckBoxes(self.driver)
        self.check_boxes.load()
        self.check_boxes.click_check_box1()
        self.check_boxes.unclick_check_box1()

    def test_context(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[6].click()

        self.context_menu = ContextMenu(self.driver)

        self.assertTrue(self.context_menu.is_alert_displayed())

    def test_drag_and_drop(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[9].click()

        self.drag_drop = DragDrop(self.driver)

        # Locate elements A and B
        element_a = self.drag_drop.find_element((By.ID, self.drag_drop.A))
        element_b = self.drag_drop.find_element((By.ID, self.drag_drop.B))

        # Get the initial text of the elements
        initial_text_a = element_a.text
        initial_text_b = element_b.text

        # Perform drag and drop action
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element_a, element_b).perform()

        # Verify the text has swapped
        time.sleep(1)  # Small delay to ensure the action is completed

        swapped_text_a = self.drag_drop.find_element((By.ID, self.drag_drop.A)).text
        swapped_text_b = self.drag_drop.find_element((By.ID, self.drag_drop.B)).text

        assert swapped_text_a == initial_text_b, f"Expected {initial_text_b}, but got {swapped_text_a}"
        assert swapped_text_b == initial_text_a, f"Expected {initial_text_a}, but got {swapped_text_b}"

    def test_dropdown(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[10].click()

        self.dropdown = DropDown(self.driver)
        # Locate the dropdown menu
        dropdown = self.dropdown.find_element((By.ID, self.dropdown.DROPDOWN))

        # Create a Select object
        select = Select(dropdown)

        # Select the first option by visible text and verify the selection
        select.select_by_visible_text("Option 1")
        selected_option = select.first_selected_option
        assert selected_option.text == "Option 1", f"Expected 'Option 1', but got '{selected_option.text}'"

    def test_dynamic_controls_click_checkbox(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[12].click()

        self.dynamic = DynamicControls(self.driver)

        self.dynamic.click_remove()
        self.dynamic.click_checkbox()

    def test_dynamic_controls_click_checkbox_after_remove(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[12].click()

        self.dynamic = DynamicControls(self.driver)

        self.dynamic.click_remove()
        self.dynamic.click_checkbox()

    def test_dynamic_controls_click_enable_and_add_text(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[12].click()

        self.dynamic = DynamicControls(self.driver)

        self.dynamic.click_enable()
        self.dynamic.write_input("stam")

    def test_dynamic_controls_write_in_disabled(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[12].click()

        self.dynamic = DynamicControls(self.driver)

        self.dynamic.write_input("stam")

    def test_file_download(self):
        self.home_page.load()
        links = self.home_page.get_all_links()
        links[16].click()

        file_download = FileDownload(self.driver)
        file_download.download_file(5)

        # Define the expected file path
        download_path = "C:\\Users\\Admin\\Downloads\\some-file.txt"  # Replace with actual file name

        # Wait for the file to be downloaded (max wait time: 30 seconds)
        wait_time = 30
        start_time = time.time()
        while not os.path.exists(download_path):
            time.sleep(1)
            if time.time() - start_time > wait_time:
                break

        # Assert the file exists
        assert os.path.exists(download_path), f"File was not downloaded to {download_path}"
        print(f"File downloaded to {download_path}")
