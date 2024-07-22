from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APIPost:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def search_post_by_keywords(self):
        """
        search post by keyword
        :return: array of posts contains the keyword
        """
        response = self._request.post_request(f"{self.config['base_url']}/search-posts",
                                              self.config["post_header"], self.config["post_data"])
        items = response.data.get("data", {}).get("items", [])
        return items

    def search_posts_by_hashtag(self):
        """
        send api request to get the posts by hashtag
        :return:
        """
        response = self._request.post_request(f"{self.config['base_url']}/search-posts-by-hashtag",
                                              self.config["post_header"], self.config["post_hashtag_data"])
        items = response.data.get("data", {}).get("items", [])
        return items

    @staticmethod
    def check_if_posts_include_word(word, posts):
        """
        check if post contains the keyword/ hashtag we're searching for
        :param word:
        :param posts:
        :return:
        """
        word_found = False
        for post in posts:
            print(post)
            if word.lower() in post["text"].lower():
                word_found = True
            else:
                word_found = False
                print("Post url without keyword:", post["postUrl"])  # Print each item for clarity
                break
        return word_found
