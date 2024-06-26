import json
from week7.summary_project_cli.book import Book


class Library:
    BOOKS_FILE = 'books.json'

    def __init__(self):
        self.books = sorted(self.load_books())

    def load_books(self):
        try:
            with open(self.BOOKS_FILE, 'r') as file:
                books_data = json.load(file)
                return [Book.from_dict(book) for book in books_data]
        except FileNotFoundError:
            print(f"File '{self.BOOKS_FILE}' not found. Starting with an empty library.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{self.BOOKS_FILE}'. Starting with an empty library.")
            return []
        except Exception as e:
            print(f"An error occurred while loading books: {e}")
            return []

    def save_books(self):
        sorted_books = sorted(self.books)
        try:
            with open(self.BOOKS_FILE, 'w') as file:
                json.dump([book.to_dict() for book in sorted_books], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving books: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def find_books_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

    def edit_book(self, old_title, new_book):
        for i, book in enumerate(self.books):
            if book.title == old_title:
                self.books[i] = new_book
                self.save_books()
                return True
        print(f"Book with title '{old_title}' not found.")
        return False

    def delete_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                self.save_books()
                print(f"Book '{title}' deleted successfully.")
                return True
        print(f"Book with title '{title}' not found.")
        return False

    def find_books_by_partial_title(self, partial_title):
        return [book for book in self.books if partial_title.lower() in book.title.lower()]

    def find_books_by_year_range(self, start_year, end_year):
        return [book for book in self.books if start_year <= book.publication_year <= end_year]

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
