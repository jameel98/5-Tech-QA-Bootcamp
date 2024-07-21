import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_posts import APIPost


class TestAPIPosts(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_posts = APIPost(api_request)
        self._config = self._api_posts.config

    def test_search_post_by_keyword(self):
        """
        Send API request to find posts by keyword
        Assert we got the correct posts data
        """
        # Arrange
        keyword = self._config["post_data"]["keyword"]  # Assuming this is the single keyword "golang"

        # Act
        items = self._api_posts.search_post_by_keywords()

        # Assert
        keyword_found = False
        for item in items:
            if keyword.lower() in item["text"].lower():
                keyword_found = True
            else:
                keyword_found = False
                print("Item text without keyword:", item["text"])  # Print each item for clarity
                break

        self.assertTrue(keyword_found, f"The keyword '{keyword}' was not found in the posts.")

    def test_search_post_by_hashtag(self):
        """
        Send API request to find posts by hashtag
        Assert we got the correct posts data
        """
        # Arrange
        hashtag = "#" + self._config["post_hashtag_data"]["hashtag"]

        # Act
        items = self._api_posts.search_posts_by_hashtag()
        # Assert
        self.assertTrue(self._api_posts.check_if_posts_include_word(hashtag, items), f"The hashtag '{hashtag}' was not found in the posts.")
