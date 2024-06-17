from flask import Flask, render_template, request, redirect, url_for
from library.library import Library
from library.book import Book

app = Flask(__name__)
library = Library()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']

        new_book = Book(title, author, int(year), genre)
        library.add_book(new_book)

        return redirect(url_for('list_books'))

    return render_template('add_book.html')


@app.route('/list_books')
def list_books():
    books = library.books
    return render_template('list_books.html', books=books)


@app.route('/edit_book/<title>', methods=['GET', 'POST'])
def edit_book(title):
    book = library.find_book_by_title(title)
    if not book:
        return f"Book '{title}' not found", 404

    if request.method == 'POST':
        new_title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']

        new_book = Book(new_title, author, int(year), genre)
        library.edit_book(title, new_book)

        return redirect(url_for('list_books'))

    return render_template('edit_book.html', book=book)


@app.route('/delete_book/<title>', methods=['POST'])
def delete_book(title):
    if library.delete_book(title):
        return redirect(url_for('list_books'))
    return f"Book '{title}' not found", 404


@app.route('/buy_book/<title>', methods=['POST'])
def buy_book(title):
    if library.buy_book(title):
        return redirect(url_for('list_books'))
    return f"Book '{title}' not found", 404


@app.route('/sell_book/<title>', methods=['POST'])
def sell_book(title):
    if library.sell_book(title):
        return redirect(url_for('list_books'))
    return f"Book '{title}' not found", 404


@app.route('/rent_book/<title>', methods=['POST'])
def rent_book(title):
    if library.rent_book(title):
        return redirect(url_for('list_books'))
    return f"Book '{title}' not found", 404


@app.route('/return_book/<title>', methods=['POST'])
def return_book(title):
    if library.return_book(title):
        return redirect(url_for('list_books'))
    return f"Book '{title}' not found", 404


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_type = request.form['search_type']
        query = request.form['query']

        if search_type == 'partial_title':
            books = library.find_books_by_partial_title(query)
        elif search_type == 'year_range':
            try:
                start_year, end_year = map(int, query.split('-'))
                books = library.find_books_by_year_range(start_year, end_year)
            except ValueError:
                books = []

        return render_template('list_books.html', books=books)

    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
