import unittest
import undetected_chromedriver as uc
from week10.youtube.infra.browser_wrapper import BrowserWrapper
from week10.youtube.infra.config_provider import ConfigProvider
from week10.youtube.infra.utils import Utils
from week10.youtube.logic.base_app_page import BaseAppPage
from week10.youtube.logic.login_page import Login
from week10.youtube.logic.video_page import VideoPage


class TestRegister(unittest.TestCase):

    def setUp(self):
        # Initialize the undetected ChromeDriver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.app_page = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_functionality(self):
        # Perform search
        self.app_page.search_video(self.config["search_input"])

        # Get search results
        results = self.app_page.get_search_results()

        # Assert that at least one result has the same title as the search query
        assert any(self.config["search_input"].lower() in result.lower() for result in results), "No matching video found in search results"

        print("Test passed: Matching video found in search results")

    def test_over_limit_search(self):
        self.app_page.search_video(Utils.generate_random_string(200))


    def test_save_video_functionality(self):
        # Perform search
        self.app_page.search_video(self.config["search_input"])

        # Wait for the video page to load
        self.video_page = VideoPage(self.driver)
        self.video_page.click_save()

        # Select "Watch Later" from the dropdown
        self.video_page.select_watch_later()
        print("vedio added")