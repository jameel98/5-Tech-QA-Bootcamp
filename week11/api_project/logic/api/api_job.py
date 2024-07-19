from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APIJob:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def search_job(self, keyword, location_id, date_posted):
        return self._request.get_request(f"{self.config['base_url']}/search-jobs?keywords={keyword}"
                                         f"&locationId={location_id}&datePosted={date_posted}&sort=mostRelevant",
                                         self.config["headers"])




