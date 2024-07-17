import requests

from week11.api_lesson.infra.config_provider import ConfigProvider


class APIWrapper:
    def __init__(self):
        self._request = None
        self.config = ConfigProvider.load_from_file('../config.json')

    def get_request(self, url, body=None):
        return requests.get(url, json=body)