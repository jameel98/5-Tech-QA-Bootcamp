import unittest

import parameterized as parameterized
import xmlrunner as xmlrunner
from xmlrunner import XMLTestRunner

from week11.api_lesson.infra.api_wrapper import APIWrapper
from week11.api_lesson.logic.api.api_deck_cards import APICards


class TestAPIHarryPotter(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self.api_cards = APICards(api_request)

    def test_shuffle_deck(self):
        # Arrange
        # Act
        response = self.api_cards.shuffle_new_deck(1)
        # Assert
        self.assertIn('deck_id', response)
        self.assertTrue(response['shuffled'])
        self.assertEqual(response['remaining'], 52)

    def test_draw_cards(self):
        # Arrange
        response = self.api_cards.shuffle_new_deck(1)
        deck_id = response['deck_id']

        # Act
        draw_response = self.api_cards.draw_card(deck_id, 2)

        # Assert
        self.assertEqual(draw_response['remaining'], 50)
        self.assertEqual(len(draw_response['cards']), 2)

    def test_reshuffle_deck(self):
        # Arrange
        response = self.api_cards.shuffle_new_deck(1)
        deck_id = response['deck_id']
        self.api_cards.draw_card(deck_id, 2)

        # Act
        reshuffle_response = self.api_cards.reshuffle_deck(deck_id)

        # Assert
        self.assertTrue(reshuffle_response['shuffled'])
        self.assertEqual(reshuffle_response['remaining'], 52)


    # @parameterized.expand([
    #     (1, 51),
    #     (2, 50),
    #     (5, 47),
    # ])
    # def test_draw_cards_parameterized(self, count, expected_remaining):
    #     # Arrange
    #     response = self.api_cards.shuffle_new_deck(1)
    #     deck_id = response['deck_id']
    #
    #     # Act
    #     draw_response = self.api_cards.draw_card(deck_id, count)
    #
    #     # Assert
    #     self.assertEqual(draw_response['remaining'], expected_remaining)
    #     self.assertEqual(len(draw_response['cards']), count)
