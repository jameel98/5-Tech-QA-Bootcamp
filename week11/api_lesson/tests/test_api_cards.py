import unittest

from week11.api_lesson.infra.api_wrapper import APIWrapper
from week11.api_lesson.logic.api.api_deck_cards import APICards


class TestAPIHarryPotter(unittest.TestCase):

    def setUp(self) -> None:

    def test_check_house_by_id(self):
        api_request = APIWrapper()
        api_cards = APICards(api_request)
        result = api_cards.shuffle_the_cards(1)
        body = result.json()

        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
