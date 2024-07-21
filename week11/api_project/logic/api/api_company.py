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
        """
        this functions sends a postrequest for the api company jobs end points
        :param company_name: input is the company name
        :return: data of jobs in the company
        """
        return self._request.post_request(f"{self.config['base_url']}/company-jobs?username={company_name}",
                                          self.config["post_header"], self.config["company_data"])

    def get_company_employees_count(self):
        return self._request.post_request(f"{self.config['base_url']}/get-company-employees-count",
                                          self.config["post_header"], self.config["company_employee_count"])

    @staticmethod
    def check_if_jobs_of_the_company(company_name, jobs):

        company_name_found = False
        for job in jobs:
            print(job)
            if company_name.lower() in job["company"]["name"].lower():
                company_name_found = True
            else:
                company_name_found = False
                print("Post text without keyword:", job["company"]["name"])  # Print each item for clarity
                break
        return company_name_found
