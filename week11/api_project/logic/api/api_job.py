from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APIJob:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def search_job(self, job):
        """
        search for job by keyword, location, date posted and sort
        :param job:
        """
        return self._request.get_request(f"{self.config['base_url']}/search-jobs?keywords={job.keywords}"
                                         f"&locationId={job.location_id}&datePosted={job.date_posted}&sort={job.sort}",
                                         self.config["headers"])

    def get_job_details(self, job_id):
        """
        get job details by the job id
        :param job_id:
        :return:
        """
        return self._request.get_request(f"{self.config['base_url']}/get-job-details?id={job_id}", self.config["headers"])


