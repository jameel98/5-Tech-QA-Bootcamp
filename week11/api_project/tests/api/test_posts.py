import logging
import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_posts import APIPost


class TestAPIPosts(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_posts = APIPost(api_request)
        self._config = self._api_posts.config
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def test_search_post_by_keyword(self):
        """
        Send API request to find posts by keyword
        Assert we got the correct posts data
        """
        logging.info(f'test_search_post_by_keyword started.')
        # Arrange
        keyword = self._config["post_data"]["keyword"]  # Assuming this is the single keyword "golang"

        # Act
        items = self._api_posts.search_post_by_keywords()

        # Assert
        self.assertTrue(self._api_posts.check_if_posts_include_word(keyword, items),
                        f"The keyword '{keyword}' was not found in the posts.")
        logging.info(f'test_search_post_by_keyword ended.')

    def test_search_post_by_hashtag(self):
        """
        Send API request to find posts by hashtag
        Assert we got the correct posts data
        """
        logging.info(f'test_search_post_by_hashtag started.')
        # Arrange
        hashtag = "#" + self._config["post_hashtag_data"]["hashtag"]
        # Act
        items = self._api_posts.search_posts_by_hashtag()
        # Assert
        self.assertTrue(self._api_posts.check_if_posts_include_word(hashtag, items),
                        f"The hashtag '{hashtag}' was not found in the posts.")
        logging.info(f'test_search_post_by_hashtag ended.')
