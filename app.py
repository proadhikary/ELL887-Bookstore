from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)
app.app_context().push()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    url = db.Column(db.String(500), nullable=False)

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        authors = request.form['authors']
        year = request.form['year']
        url = request.form['url']

        new_book = Book(title=title, authors=authors, year=year, url=url)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
