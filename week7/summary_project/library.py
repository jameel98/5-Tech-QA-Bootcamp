import json

from week7.summary_project.book import Book


class Library:
    BOOKS_FILE = r'C:\Users\Admin\PycharmProjects\AI\automation project\week7\summary_project\books.json'

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.BOOKS_FILE, 'r') as file:
                books_data = json.load(file)
                return [Book.from_dict(book) for book in books_data]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.BOOKS_FILE, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if not found_books:
            print(f"No books found by author: {author}")
        else:
            for book in found_books:
                print(book)

    def find_books_by_genre(self, genre):
        found_books = [book for book in self.books if book.genre == genre]
        if not found_books:
            print(f"No books found in genre: {genre}")
        else:
            for book in found_books:
                print(book)

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
