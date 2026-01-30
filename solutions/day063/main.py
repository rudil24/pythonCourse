from flask import Flask, render_template, request, redirect, url_for

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
# Code up the main.py index.html and add.html so that the following requirements are met:

# CHALLENGE 1
# When you head over to http://locahost:5000 (or whatever shows up as your URL when you run main.py), you should have a <h1> that says My Library and link <a> to Add New Book.

# CHALLENGE 2
# When you head over to the /add path, e.g. http://locahost:5000/add you should see a form like the one in ./docs/day063_challenge2.webp

# CHALLENGE 3
# Make the form on the /add path work so that when you click "Add Book" the book details gets added as a dictionary to the list called all_books in main.py.
# The data structure of all_books should be a List of Dictionary objects. e.g:
#   all_books = [
#          {
#             "title": "Harry Potter",
#             "author": "J. K. Rowling",
#             "rating": 9,
#        }
#   ]
# CHALLENGE 4
# Make the home page show each of the books in all_books as a list item <li> in an unordered list <ul> e.g. like the snapshot of the webpage in ./docs/day063_challenge2.webp
#
# CHALLENGE 5
# Make the home page show <p>Library is empty.</p> if there are no books. Also, make sure the "Add New Book" link works and takes the user to the /add page.
# Hint: If there are no books then all_books = []

# # "old" code for challenges 1-5 when we were storing to lists instead of db.
# # i imagine we'll re-use some of the code.
# app = Flask(__name__)

# all_books = []


# @app.route("/")
# def home():
#     return render_template("index.html", books=all_books)


# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         new_book = {
#             "title": request.form["title"],
#             "author": request.form["author"],
#             "rating": request.form["rating"],
#         }
#         all_books.append(new_book)
#         return redirect(url_for("home"))
#     return render_template("add.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


##CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
