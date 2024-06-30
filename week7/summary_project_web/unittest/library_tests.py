import unittest
import os
import json
from unittest.mock import patch
from week7.summary_project_web.library.library import Library
from week7.summary_project_web.library.book import Book
from week7.summary_project_web.library.genre import Genre


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.test_books_file = 'books.json'
        self.library = Library()

    def tearDown(self):
        if os.path.exists(self.test_books_file):
            os.remove(self.test_books_file)

    # test library functionality
    def test_initialization_with_existing_file(self):
        # Arrange
        # initial books
        book1 = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        book2 = Book("Animal Farm", "George Orwell", 1945, Genre.ACTION)
        # add book to the library
        self.library.books = [book1, book2]
        # save books
        self.library.save_books()

        # Act
        books = self.library.load_books()

        print(f"Loaded books: {[book.__dict__ for book in books]}")  # Debug print
        # Assert
        self.assertEqual(len(books), 2)

    def test_initialization_with_missing_file(self):
        # Arrange
        self.library.BOOKS_FILE = ""

        # Act
        books = self.library.load_books()

        # Assert
        self.assertEqual(len(books), 0)

    def test_save_book(self):
        # Arrange
        # initial books
        book1 = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        # add book to the library
        self.library.books = [book1]
        # save books
        self.library.save_books()

        # Act
        books = self.library.load_books()

        print(f"Loaded books: {[book.__dict__ for book in books]}")  # Debug print
        # Assert
        self.assertEqual(len(books), 1)

    def test_save_books_invalid_Genre(self):
        # Arrange
        book = Book("1984", "George Orwell", 1949, "pop")
        self.library.books.append(book)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.save_books()

        self.assertEqual(str(context.exception), "Genre must be an instance of Genre Enum, got <class 'str'>")

    def test_save_books_invalid_book_name(self):
        # Arrange
        book = Book("@#1984", "George Orwell", 1949, Genre.DRAMA)
        self.library.books.append(book)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.save_books()

        self.assertEqual(str(context.exception), "title must contain alphabet and numbers only")

    def test_save_books_invalid_author_name(self):
        # Arrange
        book = Book("1984", "George 123", 1949, Genre.DRAMA)
        self.library.books.append(book)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.save_books()

        self.assertEqual(str(context.exception), "author name must contain alphabet only")

    def test_save_books_invalid_year(self):
        # Arrange
        book = Book("1984", "George", 19491, Genre.DRAMA)
        self.library.books.append(book)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.save_books()

        self.assertEqual(str(context.exception), "publication year must be number and less than 2025")

    def test_edit_book(self):
        # Arrange
        # initial books
        book = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        new_book = Book("pop 123", "George Orwell", 1949, Genre.ACTION)

        # add book to the library
        self.library.books = [book]
        # save books
        self.library.save_books()

        # Act
        self.library.edit_book("1984", new_book)

        # Assert
        self.assertEqual(self.library.books.pop().title, "pop 123")

    def test_edit_book_invalid_title(self):
        # Arrange
        book = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        new_book = Book("@#pop 123", "George Orwell", 1949, Genre.ACTION)
        self.library.books = [book]
        self.library.save_books()

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.edit_book("1984", new_book)
        self.assertEqual(str(context.exception), "title must contain alphabet and numbers only")

    def test_edit_book_invalid_author(self):
        # Arrange
        book = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        new_book = Book("pop 123", "123 Orwell", 1949, Genre.ACTION)
        self.library.books = [book]
        self.library.save_books()

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.edit_book("1984", new_book)
        self.assertEqual(str(context.exception), "author name must contain alphabet only")

    def test_edit_book_invalid_year(self):
        # Arrange
        book = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        new_book = Book("pop 123", "George Orwell", 19491, Genre.ACTION)
        self.library.books = [book]
        self.library.save_books()

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.edit_book("1984", new_book)
        self.assertEqual(str(context.exception), "publication year must be number and less than 2025")

    def test_edit_book_invalid_genre(self):
        # Arrange
        book = Book("1984", "George Orwell", 1949, Genre.DRAMA)
        new_book = Book("pop 123", "George Orwell", 1949, "badd")
        self.library.books = [book]
        self.library.save_books()

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.library.edit_book("1984", new_book)
        self.assertEqual(str(context.exception), "Genre must be an instance of Genre Enum, got <class 'str'>")

    def test_list_books(self):
        # Arrange
        book1 = Book("pop", "George Orwell", 1949, Genre.COMEDY)
        book2 = Book("konan", "George Orwell", 1949, Genre.ACTION)
        book3 = Book("naruto", "George Orwell", 1949, Genre.DRAMA)
        # add book to the library
        self.library.books = [book1, book2, book3]
        # save books
        self.library.save_books()

        # Act
        books_list = self.library.list_books()

        # Assert
        self.assertEqual(len(books_list), 3)

    #
    def test_search_books_by_title(self):
        # Arrange
        book1 = Book("pop", "George Orwell", 1949, Genre.DRAMA)
        book2 = Book("konan", "George Orwell", 1949, Genre.ACTION)
        book3 = Book("naruto", "George Orwell", 1949, Genre.COMEDY)
        # add book to the library
        self.library.books = [book1, book2, book3]
        # save books
        self.library.save_books()

        # Act
        books_found = self.library.find_book_by_title("pop")

        # Assert
        self.assertIsNotNone(books_found)
        self.assertEqual(books_found.title, "pop")

    def test_search_books_by_partial_title(self):
        book1 = Book("pop", "George Orwell", 1949, Genre.DRAMA)
        book2 = Book("konan", "George Orwell", 1949, Genre.ACTION)
        book3 = Book("naruto", "George Orwell", 1949, Genre.COMEDY)
        # add book to the library
        self.library.books = [book1, book2, book3]
        # save books
        self.library.save_books()

        # Act
        books_found = self.library.find_books_by_partial_title("p")

        # Assert
        self.assertIsNotNone(books_found)
        for book in books_found:
            with self.subTest(book=book):
                self.assertIn("p", book.title.lower())

def test_search_books_by_author(self):
    # Arrange

    book1 = Book("1984", "George Orwell", 1949, Genre.DRAMA)
    book2 = Book("Animal Farm", "George Orwell", 1945, Genre.ACTION)

    self.library.books = [book1, book2]

    # Act
    books_found = self.library.find_books_by_author("George Orwell")

    # Assert
    self.assertEqual(len(books_found), 2)


def test_delete_book(self):
    # Arrange
    book1 = ["1984", "George Orwell", 1949, Genre.DRAMA]
    book2 = ["Animal Farm", "George Orwell", 1945, Genre.ACTION]
    self.library.books = [book1, book2]

    # Act
    self.library.delete_book("1984")

    # Assert
    books_found = self.library.find_book_by_title("1984")
    self.assertIsNone(books_found)
    self.assertEqual(len(self.library.books), 1)
