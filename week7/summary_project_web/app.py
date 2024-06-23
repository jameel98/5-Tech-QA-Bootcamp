from flask import Flask, render_template, request, redirect, url_for
from week7.summary_project_cli.library import Library
from week7.summary_project_cli.book import Book
from week7.summary_project_web.library.utils import Utils

app = Flask(__name__)
library = Library()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books')
def list_books():
    books = sorted(library.books)
    return render_template('list_books.html', books=books)


def handle_add_book(request):
    title = request.form['title']
    author = request.form['author']
    publication_year = request.form['publication_year']
    genre = request.form['genre']

    if not Utils.validate_book_name(title):
        return "Invalid title. Please enter a valid title (letters, numbers, spaces, and hyphens allowed)."
    if not Utils.validate_name(author):
        return "Invalid author name. Please enter a valid name (letters, spaces, and hyphens allowed)."
    if not Utils.validate_year(publication_year):
        return "Invalid publication year. Please enter a valid four-digit year."
    if not Utils.validate_name(genre):
        return "Invalid genre. Please enter a valid genre (letters, spaces, and hyphens allowed)."

    new_book = Book(title, author, int(publication_year), genre)
    library.add_book(new_book)
    return None


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        error = handle_add_book(request)
        if error:
            return render_template('add_book.html', error=error)
        return redirect(url_for('list_books'))
    return render_template('add_book.html')


def handle_edit_book(request, book):
    new_title = request.form['title']
    author = request.form['author']
    publication_year = request.form['publication_year']
    genre = request.form['genre']

    if not Utils.validate_book_name(new_title):
        return "Invalid title. Please enter a valid title (letters, numbers, spaces, and hyphens allowed)."
    if not Utils.validate_name(author):
        return "Invalid author name. Please enter a valid name (letters, spaces, and hyphens allowed)."
    if not Utils.validate_year(publication_year):
        return "Invalid publication year. Please enter a valid four-digit year."
    if not Utils.validate_name(genre):
        return "Invalid genre. Please enter a valid genre (letters, spaces, and hyphens allowed)."

    book.title = new_title
    book.author = author
    book.publication_year = int(publication_year)
    book.genre = genre
    library.save_books()
    return None


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    book = library.find_book_by_title(title)
    if request.method == 'POST':
        error = handle_edit_book(request, book)
        if error:
            return render_template('edit_book.html', book=book, error=error)
        return redirect(url_for('list_books'))
    return render_template('edit_book.html', book=book)


@app.route('/delete/<title>', methods=['POST'])
def delete_book(title):
    library.delete_book(title)
    return redirect(url_for('list_books'))


def handle_search_books(request):
    search_type = request.form['search_type']
    query = request.form['query']
    results = []

    if search_type == 'partial_title':
        results = library.find_books_by_partial_title(query)
    elif search_type == 'year_range':
        try:
            start_year, end_year = map(int, query.split('-'))
            results = library.find_books_by_year_range(start_year, end_year)
        except ValueError:
            results = []

    return results, query, search_type


@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        results, query, search_type = handle_search_books(request)
        return render_template('search_results.html', results=results, query=query, search_type=search_type)
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
