import requests

from week11.api_project.infra.config_provider import ConfigProvider


class APIWrapper:
    def __init__(self):
        self._request = None
        self.config = ConfigProvider.load_from_file('../../config.json')

    @staticmethod
    def get_request(url, header, body=None):
        return requests.get(url, headers=header, json=body)

    @staticmethod
    def post_request(url, header, body=None):
        return requests.post(url, headers=header, json=body)
