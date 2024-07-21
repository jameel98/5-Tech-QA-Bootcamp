from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APIPost:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def search_post_by_keywords(self):
        response = self._request.post_request(f"{self.config['base_url']}/search-posts",
                                              self.config["post_header"], self.config["post_data"])
        response_data = response.json()
        items = response_data.get("data", {}).get("items", [])
        return items

    def search_posts_by_hashtag(self):
        response = self._request.post_request(f"{self.config['base_url']}/search-posts-by-hashtag",
                                              self.config["post_header"], self.config["post_hashtag_data"])
        response_data = response.json()
        items = response_data.get("data", {}).get("items", [])
        return items

    @staticmethod
    def check_if_posts_include_word(word, posts):

        word_found = False
        for post in posts:
            print(post)
            if word.lower() in post["text"].lower():
                word_found = True
            else:
                word_found = False
                print("Post text without keyword:", post["text"])  # Print each item for clarity
                break
        return word_found
