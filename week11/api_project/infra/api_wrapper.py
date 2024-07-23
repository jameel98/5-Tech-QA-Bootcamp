import logging

import requests

from week11.api_project.infra.config_provider import ConfigProvider
from week11.api_project.infra.response_wrapper import ResponseWrapper


class APIWrapper:
    def __init__(self):
        self._request = None
        self.config = ConfigProvider.load_from_file('../../config.json')
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    @staticmethod
    def get_request(url, header, body=None):
        logging.info(f'send api get request.')
        result = requests.get(url, headers=header, json=body)
        return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())

    @staticmethod
    def post_request(url, header, body=None):
        logging.info(f'send api post request.')
        result = requests.post(url, headers=header, json=body)
        return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
