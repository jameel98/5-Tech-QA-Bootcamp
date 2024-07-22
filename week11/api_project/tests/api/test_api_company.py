import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_company import APICompany


class TestAPICompany(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_company = APICompany(api_request)
        self._config = self._api_company.config

    def test_company_details(self):
        """
        send api request to find company by name
        assert we got correct company profile data
        :return:
        """
        # Arrange
        # Act
        response = self._api_company.get_company_details(self._config["company_name"])
        # for presentation
        response_data = response.json()
        print(response_data)
        # Assert
        self.assertEqual(response_data["data"]["name"], self._config["company_name"])

    def test_company_jobs(self):
        # Arrange
        # Act
        response = self._api_company.get_company_jobs(self._config["company_name"])
        # for presentation
        response_data = response.json()
        print(response_data)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_data["data"]["total"])

    def test_get_company_employees_count(self):
        # Arrange
        # act
        response = self._api_company.get_company_employees_count()
        # assert
        self.assertEqual(response.status_code, 200)
