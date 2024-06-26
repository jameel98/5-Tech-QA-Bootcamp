from week7.summary_project_web.library.utils import Utils


class Book:
    def __init__(self, title, author, publication_year, genre):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre

    # Property for title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    # Property for author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    # Property for publication_year
    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        self._publication_year = publication_year

    # Property for genre
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def to_dict(self):
        return {
            'title': self._title,
            'author': self._author,
            'publication_year': self._publication_year,
            'genre': self._genre
        }

    # function to read data from dict
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['title'],
            data['author'],
            data['publication_year'],
            data['genre']
        )

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
