from week7.summary_project_web.library.genre import Genre
from week7.summary_project_web.library.utils import Utils


class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    # Property for title
    @property
    def title(self):
        return self._title

    # adding verifications in setters
    @title.setter
    def title(self, title):
        if Utils.validate_book_name(title):
            self._title = title
        else:
            raise ValueError(f"title must contain alphabet and numbers only")

    # Property for author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if Utils.validate_name(author):
            self._author = author
        else:
            raise ValueError(f"author name must contain alphabet only")

    # Property for publication_year
    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        if Utils.validate_year(publication_year):
            self._publication_year = publication_year
        else:
            raise ValueError(f"publication year must be number and less than 2025")

    # Property for genre
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, Genre):
            self._genre = genre
        else:
            raise ValueError(f"Genre must be an instance of Genre Enum, got {type(genre)}")

    def to_dict(self):
        return {
            'title': self._title,
            'author': self._author,
            'publication_year': self._publication_year,
            'genre': self._genre.value
        }

    @classmethod
    def from_dict(cls, data):
        try:
            # Ensure 'genre' is converted to Genre Enum
            genre_str = data['genre']
            genre = Genre(genre_str)  # This correctly maps the string to the Genre Enum
            return cls(
                data['title'],
                data['author'],
                data['publication_year'],
                genre
            )
        except KeyError as e:
            raise ValueError(f"Invalid data format: Missing required field '{e.args[0]}'")
        except ValueError as e:
            raise ValueError(f"Invalid data format: {str(e)}")

    # print data
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Genre: {self.genre}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author and
                    self.publication_year == other.publication_year and
                    self.genre == other.genre)
        return NotImplemented
