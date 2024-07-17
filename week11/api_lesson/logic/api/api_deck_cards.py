from week11.api_lesson.infra.api_wrapper import APIWrapper
from week11.api_lesson.infra.config_provider import ConfigProvider


class APICards:
    def __init__(self, request: APIWrapper):
        self._request = request

        self.config = ConfigProvider.load_from_file('../config.json')

    def shuffle_the_cards(self, num):
        return self._request.get_request(f"{self.config['api']}/new/shuffle/?deck_count={num}")

    def draw_card(self, deck_id):
        return self._request.get_request(f"{self.config['api']}/{deck_id}/draw/?count=2")
