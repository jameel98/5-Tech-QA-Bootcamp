import json
import os

from week7.summary_project_web.library.book import Book
from week7.summary_project_web.library.genre import Genre
from week7.summary_project_web.library.utils import Utils


class Library:
    BOOKS_FILE = 'books.json'

    def __init__(self):
        self.books = []
        if not os.path.exists(self.BOOKS_FILE):
            self.save_books()  # Create an empty file if it doesn't exist
        self.load_books()

    def load_books(self):
        try:
            with open(self.BOOKS_FILE, 'r') as file:
                books_data = json.load(file)
                if not isinstance(books_data, list):
                    raise ValueError(f"Expected a list of books, but got: {type(books_data)}")
                return [Book.from_dict(book) for book in books_data]
        except FileNotFoundError:
            print(f"File '{self.BOOKS_FILE}' not found. Starting with an empty library.")
            return []
        except json.JSONDecodeError as json_error:
            print(f"Error decoding JSON from file '{self.BOOKS_FILE}': {json_error}")
            return []
        except ValueError as value_error:
            print(f"Value error loading books from '{self.BOOKS_FILE}': {value_error}")
            return []
        except Exception as e:
            print(f"An error occurred while loading books: {e}")
            return []

    def save_books(self):
        try:
            with open(self.BOOKS_FILE, 'w') as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving books: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def list_books(self):
        if not self.books:
            return []
        else:
            return self.books

    # adding search method
    def search_books(self, search_type, search_value):
        search_funcs = {
            'title': lambda book: book.title == search_value,
            'partial_title': lambda book: search_value.lower() in book.title.lower(),
            'author': lambda book: book.author == search_value,
            'genre': lambda book: book.genre == search_value,
            'year_range': lambda book: search_value[0] <= book.publication_year <= search_value[1]
        }

        if search_type not in search_funcs:
            raise ValueError(f"Unknown search type: {search_type}")

        return list(filter(search_funcs[search_type], self.books))

    def find_book_by_title(self, title):
        books = self.search_books('title', title)
        return books[0] if books else None

    def find_books_by_author(self, author):
        return self.search_books('author', author)

    def find_books_by_genre(self, genre):
        return self.search_books('genre', genre)

    def find_books_by_partial_title(self, partial_title):
        return self.search_books('partial_title', partial_title)

    def find_books_by_year_range(self, start_year, end_year):
        return self.search_books('year_range', (start_year, end_year))

    def edit_book(self, old_title, new_book):
        index = next((i for i, book in enumerate(self.books) if book.title == old_title), None)
        if index is not None:
            self.books[index] = new_book
            self.save_books()
            return True
        else:
            print(f"Book with title '{old_title}' not found.")
            return False

    def delete_book(self, title):
        book = self.find_book_by_title(title)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        else:
            print(f"Book with title '{title}' not found.")
            return False

    def edit_book_detail(self, title, detail, new_value):
        book = self.find_book_by_title(title)
        if book:
            if detail == 'title':
                book.title = new_value
            elif detail == 'author':
                book.author = new_value
            elif detail == 'year':
                book.publication_year = new_value
            elif detail == 'genre':
                book.genre = new_value
            self.save_books()
            print(f"Book '{title}' {detail} updated to '{new_value}'.")
        else:
            print(f"Book with title '{title}' not found.")

    def handle_add_book(self, form_data):
        title = form_data['title']
        author = form_data['author']
        publication_year = form_data['publication_year']
        genre_str = form_data['genre']  # Assuming genre_str is passed from form data

        genre_enum = Genre[genre_str]  # Convert string to Genre enum
        new_book = Book(title, author, publication_year, genre_enum)
        self.add_book(new_book)

    def handle_edit_book(self, form_data, book):
        new_title = form_data['title']
        author = form_data['author']
        publication_year = form_data['publication_year']
        genre_str = form_data['genre']  # Assuming genre_str is passed from form data

        genre_enum = Genre[genre_str]  # Convert string to Genre enum
        book.title = new_title
        book.author = author
        book.publication_year = publication_year
        book.genre = genre_enum
        self.save_books()

    def handle_search_books(self, form_data):
        search_type = form_data['search_type']
        query = form_data['query']
        results = []

        if search_type == 'partial_title':
            results = self.find_books_by_partial_title(query)
        elif search_type == 'year_range':
            try:
                start_year, end_year = map(int, query.split('-'))
                results = self.find_books_by_year_range(start_year, end_year)
            except ValueError:
                results = []

        return results, query, search_type
