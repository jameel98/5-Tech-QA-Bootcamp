from flask import Flask, render_template, request, redirect, url_for
from week7.summary_project.library import Library
from week7.summary_project.book import Book

app = Flask(__name__)
library = Library()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books')
def list_books():
    books = sorted(library.books)
    return render_template('list_books.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        genre = request.form['genre']
        new_book = Book(title, author, int(publication_year), genre)
        library.add_book(new_book)
        return redirect(url_for('list_books'))
    return render_template('add_book.html')


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    book = library.find_book_by_title(title)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.publication_year = int(request.form['publication_year'])
        book.genre = request.form['genre']
        library.save_books()
        return redirect(url_for('list_books'))
    return render_template('edit_book.html', book=book)


@app.route('/delete/<title>', methods=['POST'])
def delete_book(title):
    library.delete_book(title)
    return redirect(url_for('list_books'))


if __name__ == '__main__':
    app.run(debug=True)
