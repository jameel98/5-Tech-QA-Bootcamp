from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APICompany:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_company_details(self, username):
        """
        this function sends GET api request to company details endpoint
        :param username: name of the company
        :return: profile data of the company
        """
        return self._request.get_request(f"{self.config['base_url']}/get-company-details?username={username}",
                                         self.config["headers"])

    def get_company_jobs(self, company_name):
        return self._request.post_request(f"{self.config['base_url']}/company-jobs?username={company_name}",
                                          self.config["company_header"], self.config["company_data"])
