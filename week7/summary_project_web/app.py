from flask import Flask, render_template, request, redirect, url_for
from week7.summary_project_web.library.library import Library

app = Flask(__name__)
library = Library()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books')
def list_books():
    books = library.list_books()
    return render_template('list_books.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        error = library.handle_add_book(request.form)
        if error:
            return render_template('add_book.html', error=error)
        return redirect(url_for('list_books'))
    return render_template('add_book.html')


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    book = library.find_book_by_title(title)
    if not book:
        return f"Book with title '{title}' not found."

    if request.method == 'POST':
        error = library.handle_edit_book(request.form, book)
        if error:
            return render_template('edit_book.html', book=book, error=error)
        return redirect(url_for('list_books'))

    return render_template('edit_book.html', book=book)


@app.route('/delete/<title>', methods=['POST'])
def delete_book(title):
    if library.delete_book(title):
        return redirect(url_for('list_books'))
    else:
        return f"Book with title '{title}' not found."


@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        results, query, search_type = library.handle_search_books(request.form)
        return render_template('search_results.html', results=results, query=query, search_type=search_type)
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
