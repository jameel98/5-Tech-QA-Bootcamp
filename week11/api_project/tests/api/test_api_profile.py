import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_profile import APIProfile


class TestAPIProfile(unittest.TestCase):

    def setUp(self) -> None:
        """
        setup the api wrapper and api profile
        and get the config profile data
        """
        api_request = APIWrapper()
        self._api_profile = APIProfile(api_request)
        self._config = self._api_profile.config

    def test_profile(self):
        """
        send api reqeust to get the user profile data by name
        assert we got the correct user profile data
        :return:
        """
        # Arrange
        # Act
        response = self._api_profile.get_profile_data(self._config["username"])
        # for presentation
        print(response.json()["firstName"])
        print(response.json())

        # Assert
        self.assertEqual(response.json()["username"], self._config["username"])
        self.assertEqual(response.json()["firstName"], self._config["firstName"])
        self.assertEqual(response.json()["lastName"], self._config["lastName"])

    def test_profile_by_url(self):
        """
        send api request to get the user profile data by URL
        assert we got the correct profile data
        :return:
        """
        # Arrange
        # Act
        response = self._api_profile.get_profile_data_by_url(self._config["profile_url"])
        # for presentation
        print(response.json()["firstName"])
        # Assert
        self.assertEqual(response.json()["username"], self._config["profile_username"])
        self.assertEqual(response.json()["firstName"], self._config["profile_firstName"])
        self.assertEqual(response.json()["lastName"], self._config["profile_lastName"])

    def test_search_people_bt_name(self):
        # arrange
        # act
        response = self._api_profile.search_people_by_name(self._config["people_name"])

        print(response.json()["items"]["0"]["fullName"])
        # assert
        self.assertIn(response.json()["items"]["0"]["fullName"], self._config["people_name"])