from week11.api_project.infra.api_wrapper import APIWrapper
from week11.api_project.infra.config_provider import ConfigProvider


class APIProfile:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_profile_data(self, username):
        """
        this functions sends GET api request to profile data endpoint
        :param username: username of the profile u searching
        :return: profile data
        """
        return self._request.get_request(f"{self.config['base_url']}/?username={username}", self.config["headers"])

    def get_profile_data_by_url(self, url):
        """
        this function sends GET request to the profile data endpoint
        :param url: of the profile u searching
        :return: profile data
        """
        return self._request.get_request(f"{self.config['base_url']}/get-profile-data-by-url?url={url}",
                                         self.config["headers"])

    def search_people_by_name(self, username):
        """
        this function sends a GET request to search people by name
        :param username: name to search
        :return: data of search result
        """
        return self._request.get_request(f"{self.config['base_url']}/search-people?keywords={username}&start=0&geo=103644278%2C101165590'",
                                         self.config["headers"])
