import unittest
from week7.summary_project_web.library.book import Book
from week7.summary_project_web.library.genre import Genre
from week7.summary_project_web.library.utils import Utils


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949, Genre.drama)

    def test_initialization(self):
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.publication_year, 1949)
        self.assertEqual(self.book.genre, Genre.drama)

    def test_title_property(self):
        self.book.title = "Animal Farm"
        self.assertEqual(self.book.title, "Animal Farm")
        with self.assertRaises(ValueError):
            self.book.title = "Animal Farm@"

    def test_author_property(self):
        self.book.author = "Eric Blair"
        self.assertEqual(self.book.author, "Eric Blair")
        with self.assertRaises(ValueError):
            self.book.author = "Eric123"

    def test_publication_year_property(self):
        self.book.publication_year = 1945
        self.assertEqual(self.book.publication_year, 1945)
        with self.assertRaises(ValueError):
            self.book.publication_year = 2025
        with self.assertRaises(ValueError):
            self.book.publication_year = "Year1945"

    def test_genre_property(self):
        self.book.genre = Genre.comedy
        self.assertEqual(self.book.genre, Genre.comedy)
        with self.assertRaises(ValueError):
            self.book.genre = "InvalidGenre"

    def test_to_dict(self):
        expected = {
            'title': "1984",
            'author': "George Orwell",
            'publication_year': 1949,
            'genre': Genre.drama
        }
        self.assertEqual(self.book.to_dict(), expected)

    def test_from_dict(self):
        data = {
            'title': "Brave New World",
            'author': "Aldous Huxley",
            'publication_year': 1932,
            'genre': Genre.history
        }
        new_book = Book.from_dict(data)
        self.assertEqual(new_book.title, "Brave New World")
        self.assertEqual(new_book.author, "Aldous Huxley")
        self.assertEqual(new_book.publication_year, 1932)
        self.assertEqual(new_book.genre, Genre.history)

    def test_str(self):
        self.assertEqual(str(self.book), "Title: 1984, Author: George Orwell, Year: 1949, Genre: Genre.drama")

    def test_eq(self):
        same_book = Book("1984", "George Orwell", 1949, Genre.drama)
        different_book = Book("Animal Farm", "George Orwell", 1945, Genre.comedy)
        self.assertTrue(self.book == same_book)
        self.assertFalse(self.book == different_book)

    def test_validate_name(self):
        self.assertTrue(Utils.validate_name("George Orwell"))
        self.assertFalse(Utils.validate_name("George123"))

    def test_validate_year(self):
        self.assertTrue(Utils.validate_year(1949))
        self.assertTrue(Utils.validate_year(2024))
        self.assertFalse(Utils.validate_year(2025))
        self.assertFalse(Utils.validate_year(3025))
        self.assertFalse(Utils.validate_year("abcd"))
        self.assertFalse(Utils.validate_year("202a"))

    def test_validate_book_name(self):
        self.assertTrue(Utils.validate_book_name("1984"))
        self.assertTrue(Utils.validate_book_name("Animal Farm"))
        self.assertFalse(Utils.validate_book_name("Animal Farm@"))

