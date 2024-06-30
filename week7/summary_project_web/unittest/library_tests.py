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

    # def tearDown(self):
    #     if os.path.exists(self.test_books_file):
    #         os.remove(self.test_books_file)

    def create_test_books_file(self, data):
        try:
            with open(self.test_books_file, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Test books file created with data: {data}")  # Debug print
        except Exception as e:
            print(f"An error occurred while saving books: {e}")

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

    def test_load_books_invalid_data_type(self):
        # Arrange
        book = Book("1984", "George Orwell",  1949,  Genre.DRAMA)
        books = self.library.books.append(book)
        self.create_test_books_file(books)

        # Act
        books = self.library.load_books()

        # Assert
        self.assertEqual(len(books), 0)

    # def test_save_books(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Political fiction"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         new_book = Book("Brave New World", "Aldous Huxley", 1932, Genre.SCIENCE_FICTION)
    #         library.add_book(new_book)
    #         library.save_books()
    #
    #     # Assert
    #     with open(self.library.BOOKS_FILE, 'r') as file:
    #         saved_books = json.load(file)
    #         self.assertEqual(len(saved_books), 3)
    #
    # def test_edit_book_valid_genre(self):
    #     # Arrange
    #     initial_book_data = {
    #         'title': 'Book Title',
    #         'author': 'Author Name',
    #         'publication_year': '2023',
    #         'genre': 'Comedy'  # Example string from form data
    #     }
    #     edited_book_data = {
    #         'title': 'Book Title Updated',
    #         'author': 'New Author Name',
    #         'publication_year': '2024',
    #         'genre': 'Action'  # Example string from form data
    #     }
    #     self.library.handle_add_book(initial_book_data)
    #     initial_book = self.library.find_book_by_title('Book Title')
    #
    #     # Act
    #     with patch('your_library_module.Utils.validate_book_name', return_value=True), \
    #             patch('your_library_module.Utils.validate_name', return_value=True), \
    #             patch('your_library_module.Utils.validate_year', return_value=True):
    #         self.library.handle_edit_book(edited_book_data, initial_book)
    #         edited_book = self.library.find_book_by_title('Book Title Updated')
    #
    #     # Assert
    #     self.assertEqual(edited_book.author, 'New Author Name')
    #     self.assertEqual(edited_book.publication_year, 2024)
    #     self.assertEqual(edited_book.genre, Genre.ACTION.value)
    #
    # def test_add_book(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         new_book = Book("Brave New World", "Aldous Huxley", 1932, Genre.SCIENCE_FICTION)
    #         library.add_book(new_book)
    #
    #     # Assert
    #     self.assertEqual(len(library.books), 2)
    #
    # def test_list_books(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Drama"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_list = library.list_books()
    #
    #     # Assert
    #     self.assertEqual(len(books_list), 2)
    #
    # def test_search_books_by_title(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_found = library.find_book_by_title("1984")
    #
    #     # Assert
    #     self.assertIsNotNone(books_found)
    #     self.assertEqual(books_found.title, "1984")
    #
    # def test_search_books_by_partial_title(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_found = library.find_books_by_partial_title("farm")
    #
    #     # Assert
    #     self.assertEqual(len(books_found), 1)
    #     self.assertEqual(books_found[0].title, "Animal Farm")
    #
    # def test_search_books_by_author(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_found = library.find_books_by_author("George Orwell")
    #
    #     # Assert
    #     self.assertEqual(len(books_found), 2)
    #
    # def test_search_books_by_genre(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_found = library.find_books_by_genre("Drama")
    #
    #     # Assert
    #     self.assertEqual(len(books_found), 1)
    #     self.assertEqual(books_found[0].title, "1984")
    #
    # def test_search_books_by_year_range(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         books_found = library.find_books_by_year_range(1940, 1950)
    #
    #     # Assert
    #     self.assertEqual(len(books_found), 2)
    #
    # def test_edit_book(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         edited_book = Book("1984", "Eric Blair", 1949, Genre.DRAMA)
    #         library.edit_book("1984", edited_book)
    #
    #     # Assert
    #     books_found = library.find_book_by_title("1984")
    #     self.assertEqual(books_found.author, "Eric Blair")
    #
    # def test_edit_book_detail(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         library.edit_book_detail("1984", "author", "Eric Blair")
    #
    #     # Assert
    #     books_found = library.find_book_by_title("1984")
    #     self.assertEqual(books_found.author, "Eric Blair")
    #
    # def test_delete_book(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         library.delete_book("1984")
    #
    #     # Assert
    #     books_found = library.find_book_by_title("1984")
    #     self.assertIsNone(books_found)
    #     self.assertEqual(len(library.books), 1)
    #
    # def test_handle_add_book_valid_data(self):
    #     # Arrange
    #     form_data = {
    #         'title': '1984',
    #         'author': 'George Orwell',
    #         'publication_year': '1949',
    #         'genre': 'Drama'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Utils.validate_book_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_year', return_value=True):
    #         library = Library()
    #         library.handle_add_book(form_data)
    #
    #     # Assert
    #     books_found = library.find_book_by_title("1984")
    #     self.assertIsNotNone(books_found)
    #     self.assertEqual(books_found.title, "1984")
    #
    # def test_handle_add_book_invalid_title(self):
    #     # Arrange
    #     form_data = {
    #         'title': 'Invalid#Title',
    #         'author': 'George Orwell',
    #         'publication_year': '1949',
    #         'genre': 'Drama'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Utils.validate_book_name', return_value=False), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_year', return_value=True):
    #         library = Library()
    #         result = library.handle_add_book(form_data)
    #
    #     # Assert
    #     self.assertEqual(result,
    #                      "Invalid title. Please enter a valid title (letters, numbers, spaces, and hyphens allowed).")
    #     books_found = library.find_book_by_title("Invalid#Title")
    #     self.assertIsNone(books_found)
    #
    # def test_handle_edit_book_valid_data(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #     form_data = {
    #         'title': '1984',
    #         'author': 'Eric Blair',
    #         'publication_year': '1949',
    #         'genre': 'Drama'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Utils.validate_book_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_year', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         book_to_edit = library.find_book_by_title("1984")
    #         library.handle_edit_book(form_data, book_to_edit)
    #
    #     # Assert
    #     edited_book = library.find_book_by_title("1984")
    #     self.assertEqual(edited_book.author, "Eric Blair")
    #
    # def test_handle_edit_book_invalid_title(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #     form_data = {
    #         'title': 'Invalid#Title',
    #         'author': 'George Orwell',
    #         'publication_year': '1949',
    #         'genre': 'Drama'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Utils.validate_book_name', return_value=False), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_name', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Utils.validate_year', return_value=True), \
    #             patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         book_to_edit = library.find_book_by_title("1984")
    #         result = library.handle_edit_book(form_data, book_to_edit)
    #
    #     # Assert
    #     self.assertEqual(result,
    #                      "Invalid title. Please enter a valid title (letters, numbers, spaces, and hyphens allowed).")
    #     edited_book = library.find_book_by_title("Invalid#Title")
    #     self.assertIsNone(edited_book)
    #
    # def test_handle_search_books_partial_title(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #     form_data = {
    #         'search_type': 'partial_title',
    #         'query': 'farm'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         results, query, search_type = library.handle_search_books(form_data)
    #
    #     # Assert
    #     self.assertEqual(len(results), 1)
    #     self.assertEqual(results[0].title, "Animal Farm")
    #     self.assertEqual(query, "farm")
    #     self.assertEqual(search_type, "partial_title")
    #
    # def test_handle_search_books_year_range(self):
    #     # Arrange
    #     initial_books = [
    #         {"title": "1984", "author": "George Orwell", "publication_year": 1949, "genre": "Drama"},
    #         {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945, "genre": "Action"}
    #     ]
    #     self.create_test_books_file(initial_books)
    #     form_data = {
    #         'search_type': 'year_range',
    #         'query': '1940-1950'
    #     }
    #
    #     # Act
    #     with patch('week7.summary_project_web.library.library.Library.BOOKS_FILE', new=self.library.BOOKS_FILE):
    #         library = Library()
    #         results, query, search_type = library.handle_search_books(form_data)
    #
    #     # Assert
    #     self.assertEqual(len(results), 2)
    #     self.assertEqual(query, "1940-1950")
    #     self.assertEqual(search_type, "year_range")
    #
    # if __name__ == '__main__':
    #     unittest.main()
