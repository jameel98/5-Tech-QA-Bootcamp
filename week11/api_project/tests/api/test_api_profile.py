import logging
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
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def test_profile(self):
        """
        send api reqeust to get the user profile data by name
        assert we got the correct user profile data
        :return:
        """
        logging.info(f'test_profile started.')
        # Arrange
        profile_data = {
            "username": "rawadabu",
            "firstName": "Rawad",
            "lastName": "AbuSaleh",
        }
        # Act
        response = self._api_profile.get_profile_data(profile_data["username"])

        # for presentation
        print(response.data["firstName"])

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], profile_data["username"])
        self.assertEqual(response.data["firstName"], profile_data["firstName"])
        self.assertEqual(response.data["lastName"], profile_data["lastName"])
        logging.info(f'test_profile ended.')

    def test_profile_by_url(self):
        """
        send api request to get the user profile data by URL
        assert we got the correct profile data
        :return:
        """
        logging.info(f'test_profile_by_url started.')
        # Arrange
        profile_data = {
            "profile_url": "https://www.linkedin.com/in/tzahi-anidgar-b8947b255/",
            "username": "tzahi-anidgar-b8947b255",
            "firstName": "Tzahi",
            "lastName": "Anidgar",
        }
        # Act
        response = self._api_profile.get_profile_data_by_url(profile_data["profile_url"])
        # for presentation
        print(response.data["firstName"])
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], profile_data["username"])
        self.assertEqual(response.data["firstName"], profile_data["firstName"])
        self.assertEqual(response.data["lastName"], profile_data["lastName"])
        logging.info(f'test_profile_by_url ended.')

    def test_search_people_by_name(self):
        """
        search people by name check if the api response containse
        profiles for people u search
        :return:
        """
        logging.info(f'test_search_people_by_name started.')
        # arrange
        username = "Sagi"
        # act
        items = self._api_profile.search_people_by_name(username)
        # assert
        self.assertTrue(self._api_profile.check_if_name_in_search_results(username, items),
                        f"The name '{username}' was not found in the items.")
        logging.info(f'test_search_people_by_name ended.')
