class Job:
    def __init__(self, keywords, location_id, date_posted, sort):
        self._keywords = keywords
        self._location_id = location_id
        self._date_posted = date_posted
        self._sort = sort

        # Getter for keywords

    @property
    def keywords(self):
        return self._keywords

    # Setter for keywords
    @keywords.setter
    def keywords(self, value):
        self._keywords = value

    # Getter for location_id
    @property
    def location_id(self):
        return self._location_id

    # Setter for location_id
    @location_id.setter
    def location_id(self, value):
        self._location_id = value

    # Getter for date_posted
    @property
    def date_posted(self):
        return self._date_posted

    # Setter for date_posted
    @date_posted.setter
    def date_posted(self, value):
        self._date_posted = value

    # Getter for sort
    @property
    def sort(self):
        return self._sort

    # Setter for sort
    @sort.setter
    def sort(self, value):
        self._sort = value