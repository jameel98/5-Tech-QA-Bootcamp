from week7.summary_project.book import Book
from week7.summary_project.library import Library


class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        self.load_library()
        while True:
            print("\n===== Library Menu =====")
            print("1. Add Book")
            print("2. List All Books")
            print("3. List Books by Author")
            print("4. List Books by Genre")
            print("5. Edit Book")
            print("6. Delete Book")
            print("7. Save Library")
            print("8. Exit")
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
                self.save_library()
            elif choice == '8':
                print("Exiting the Library App. Goodbye!")
                break
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
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
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
        title = input("Enter title of the book to edit: ")
        new_title = input("Enter new title: ")
        author = input("Enter author: ")
        publication_year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
        new_book = Book(new_title, author, publication_year, genre)
        if self.library.edit_book(title, new_book):
            print(f"Book '{title}' edited successfully.")
        else:
            print(f"Failed to edit book '{title}'.")

    def delete_book(self):
        title = input("Enter title of the book to delete: ")
        if self.library.delete_book(title):
            print(f"Book '{title}' deleted successfully.")

