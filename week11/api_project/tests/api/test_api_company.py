import logging
import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_company import APICompany


class TestAPICompany(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_company = APICompany(api_request)
        self._config = self._api_company.config
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def test_company_details(self):
        """
        send api request to find company by name
        assert we got correct company profile data
        :return:
        """
        logging.info(f'test_company_details started.')
        # Arrange
        # Act
        response = self._api_company.get_company_details(self._config["company_name"])
        # for presentation
        print(response.data)
        # Assert
        self.assertEqual(response.data["data"]["name"].lower(), self._config["company_name"])
        logging.info(f'test_company_details ended.')

    def test_company_jobs(self):
        """
        get company jobs by company name and company id
        :return:
        """
        logging.info(f'test_company_jobs started.')
        # Arrange
        # Act
        response = self._api_company.get_company_jobs(self._config["company_name"])
        # for presentation
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["data"]["items"])
        logging.info(f'test_company_jobs ended.')

    def test_get_company_employees_count(self):
        """
        get the company jobs number
        """
        logging.info(f'test_get_company_employees_count started.')
        # Arrange
        # act
        response = self._api_company.get_company_employees_count()
        # assert
        self.assertEqual(response.status_code, 200)
        logging.info(f'test_get_company_employees_count ended.')

