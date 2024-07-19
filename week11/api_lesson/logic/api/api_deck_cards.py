from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APICards:
    def __init__(self, request: APIWrapper):
        self._request = request

        self.config = ConfigProvider.load_from_file('../config.json')

    def shuffle_new_deck(self, num):
        return self._request.get_request(f"{self.config['base_url']}/new/shuffle/?deck_count={num}")

    def draw_card(self, deck_id, count=1):
        return self._request.get_request(f"{self.config['base_url']}/{deck_id}/draw/?count={count}")

    def reshuffle_deck(self, deck_id):
        return self._request.get_request(f"{self.config['base_url']}/{deck_id}/shuffle/")

    def new_brand_deck(self):
        return self._request.get_request(f"{self.config['base_url']}/new/")

    def add_to_pile(self, deck_id, pile_name, cards):
        return self._request.get_request(f"{self.config['base_url']}/{deck_id}/pile/{pile_name}/add/params={'cards': ','.join(cards)}")

    def list_pile(self, deck_id, pile_name):
        return self._request.get_request(f"{self.config['base_url']}{deck_id}/pile/{pile_name}/list/")

    def draw_from_pile(self, deck_id, pile_name, count=1):
        return self._request.get_request(f"{self.config['base_url']}/{deck_id}/pile/{pile_name}/draw/params={'count': count}")