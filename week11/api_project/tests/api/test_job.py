import logging
import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.logger_setup import LogSetup
from week11.api_project.logic.api.api_job import APIJob
from week11.api_project.logic.job import Job


class TestAPISearch(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self._api_job = APIJob(api_request)
        self._config = self._api_job.config
        log_setup = LogSetup()
        self.logger = log_setup.logger

    def test_search_job(self):
        """
        search for most relevant jobs according to its keyword
        :return:
        """
        self.logger.info(f'test_search_job started.')
        # Arrange
        job = Job(self._config["job_params"]["keywords"], self._config["job_params"]["locationId"],
                  self._config["job_params"]["datePosted"], self._config["job_params"]["sort"])
        # Act
        response = self._api_job.search_job(job)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.logger.info(f'test_search_job ended.')

    def test_job_details(self):
        """
        get job details by job ID
        :return:
        """
        self.logger.info(f'test_job_details started.')
        # Arrange
        # Act
        response = self._api_job.get_job_details(self._config["job_id"])
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._config["job_id"], response.data["data"]["id"])
        self.logger.info(f'test_job_details ended.')
