import unittest

from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.logic.api.api_job import APIJob


class TestAPISearch(unittest.TestCase):

    def setUp(self) -> None:
        api_request = APIWrapper()
        self.api_job = APIJob(api_request)

    def test_search_job(self):
        # Arrange
        # Act
        response = self.api_job.search_job("golang", 92000000, "anyTime")
        # Assert
        print(response.json())

