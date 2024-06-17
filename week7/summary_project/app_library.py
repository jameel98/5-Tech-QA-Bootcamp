from week7.summary_project.book import Book
from week7.summary_project.library import Library
from week7.summary_project.utils import Utils

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        app_run = True
        self.load_library()
        while app_run:
            print("\n===== Library Menu =====")
            print("1. Add Book")
            print("2. List All Books")
            print("3. List Books by Author")
            print("4. List Books by Genre")
            print("5. Edit Book")
            print("6. Delete Book")
            print("7. Search Books by Partial Title")
            print("8. Search Books by Year Range")
            print("9. Import Books from CSV")
            print("10. Export Books to CSV")
            print("11. Save Library")
            print("12. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_all_books()
            elif choice == '3':
                self.list_books_by_author()
            elif choice == '4':
                self.list_books_by_genre()
            elif choice == '5':
                self.edit_book()
            elif choice == '6':
                self.delete_book()
            elif choice == '7':
                self.search_books_by_partial_title()
            elif choice == '8':
                self.search_books_by_year_range()
            elif choice == '9':
                self.save_library()
            elif choice == '10':
                print("Exiting the Library App. Goodbye!")
                app_run = False
            else:
                print("Invalid choice. Please try again.")

    def load_library(self):
        print("Loading library...")
        self.library.load_books()
        print("Library loaded successfully.")

    def save_library(self):
        print("Saving library...")
        self.library.save_books()
        print("Library saved successfully.")

    def add_book(self):
        print("\n=== Add New Book ===")

        title = self.get_new_title()
        author = self.get_valid_author()
        publication_year = self.get_valid_year()
        genre = self.get_valid_genre()

        new_book = Book(title, author, publication_year, genre)
        self.library.add_book(new_book)
        print("Book added successfully.")

    def list_all_books(self):
        print("\n=== All Books in the Library ===")
        self.library.list_books()

    def list_books_by_author(self):
        author = input("Enter author name: ")
        print(f"\n=== Books by Author: {author} ===")
        self.library.find_books_by_author(author)

    def list_books_by_genre(self):
        genre = input("Enter genre: ")
        print(f"\n=== Books in Genre: {genre} ===")
        self.library.find_books_by_genre(genre)

    def edit_book(self):
        print("\n=== Edit Book ===")

        title = self.get_exist_title()
        if not self.library.find_book_by_title(title):
            print(f"Book '{title}' does not exist.")
            return

        new_title = self.get_new_title()
        author = self.get_valid_author()
        publication_year = self.get_valid_year()
        genre = self.get_valid_genre()

        new_book = Book(new_title, author, publication_year, genre)
        if self.library.edit_book(title, new_book):
            print(f"Book '{title}' edited successfully.")
        else:
            print(f"Failed to edit book '{title}'.")

    def delete_book(self):
        title = self.get_exist_title()
        if self.library.delete_book(title):
            print(f"Book '{title}' deleted successfully.")
        else:
            print(f"Failed to delete book '{title}'.")

    def get_exist_title(self):
        while True:
            title = input("Enter title: ")
            if self.library.find_book_by_title(title):
                return title
            print(f"Book '{title}' does not exist. Please enter a valid book title.")

    def get_new_title(self):
        while True:
            title = input("Enter title: ")
            if not Utils.validate_book_name(title):
                print("Invalid title. Please enter a valid title (letters, numbers, spaces, and hyphens allowed).")
                continue
            if self.library.find_book_by_title(title):
                print("Book already exists.")
            else:
                return title

    @staticmethod
    def get_valid_year():
        while True:
            try:
                publication_year = int(input("Enter publication year: "))
                if Utils.validate_year(str(publication_year)):
                    return publication_year
                print("Invalid publication year. Please enter a valid four-digit year.")
            except ValueError:
                print("Invalid input. Please enter a numeric year.")

    @staticmethod
    def get_valid_author():
        while True:
            author = input("Enter author: ")
            if Utils.validate_name(author):
                return author
            print("Invalid author name. Please enter a valid name (letters, spaces, and hyphens allowed).")

    @staticmethod
    def get_valid_genre():
        while True:
            genre = input("Enter genre: ")
            if Utils.validate_name(genre):
                return genre
            print("Invalid genre. Please enter a valid genre (letters, spaces, and hyphens allowed).")

    def search_books_by_partial_title(self):
        partial_title = input("Enter partial title: ")
        self.library.find_books_by_partial_title(partial_title)

    def search_books_by_year_range(self):
        start_year = int(input("Enter start year: "))
        end_year = int(input("Enter end year: "))
        self.library.find_books_by_year_range(start_year, end_year)