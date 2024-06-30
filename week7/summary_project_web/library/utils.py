import re


class Utils:
    @staticmethod
    def validate_name(name):
        # Regex to check if the name contains only alphabet letters (both cases)
        pattern = r'^[A-Za-z\s-]+$'
        return bool(re.match(pattern, name))

    @staticmethod
    def validate_year(year):
        if re.fullmatch(r'\d{1,4}', str(year)) and int(year) < 2025:
            return True
        return False

    @staticmethod
    def validate_book_name(name):
        # Regex to check if the name contains alphabet letters, numbers, spaces, and hyphens
        pattern = r'^[A-Za-z0-9\s-]+$'
        return bool(re.match(pattern, name))

