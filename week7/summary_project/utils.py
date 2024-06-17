import re


class Utils:
    @staticmethod
    def validate_name(name):
        # Regex to check if the name contains only alphabet letters (both cases)
        pattern = r'^[A-Za-z\s-]+$'
        return bool(re.match(pattern, name))

    @staticmethod
    def validate_year(year):
        # Regex to check if the year is a four-digit number
        pattern = r'^\d{4}$'
        return bool(re.match(pattern, year))

    @staticmethod
    def validate_book_name(name):
        # Regex to check if the name contains alphabet letters, numbers, spaces, and hyphens
        pattern = r'^[A-Za-z0-9\s-]+$'
        return bool(re.match(pattern, name))
