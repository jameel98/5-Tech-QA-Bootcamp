import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_job import APIJob


class TestAPISearch(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_job = APIJob(api_request)
        self._config = self._api_job.config

    def test_search_job(self):
        # Arrange
        # Act
        response = self._api_job.search_job(self._config["job_params"]["keywords"], self._config["job_params"]["locationId"],
                                            self._config["job_params"]["datePosted"], self._config["job_params"]["sort"])

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_job_details(self):
        # Arrange
        # Act
        response = self._api_job.get_job_details(self._config["job_id"])
        # Assert
        self.assertEqual(self._config["job_id"], response.json()["data"]["id"])
