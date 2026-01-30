# CRUD Operations with SQLAlchemy
Hopefully, you figured out how to solve the challenge from the last lesson, as a review, here's a summary of some of the things we did:

## Create a New Database
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
 
app = Flask(__name__)
 
class Base(DeclarativeBase):
    pass
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
```
As of flask-sqlalchemy version 3.1, you need to pass a subclass of DeclarativeBase to the constructor of the database.

## Create a New Table
Next we define and create the model. What is the : used for? Explicitly declaring a variable type. Below we are explicitly saying that id is of type Mapped. SQLAlchemy uses the generic Mapped so that it can type check the data that will be stored in the database.

```
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
 
with app.app_context():
    db.create_all()
```
In addition to these things, the most crucial thing to figure out when working with any new database technology is how to CRUD data records.

> **C**reate <br>
> **R**ead <br>
> **U**pdate <br>
> **D**elete <br>

So, let's go through each of these using SQLite and SQLAlchemy:
## Create A New Record
```
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
```
NOTE: When creating new records, the primary key fields is optional. you can also write:
```
new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
```
the id field will be auto-generated.
## Read All Records
```
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
```
To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows.
## Read A Particular Record By Query
```
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
```
To get a single element we can use scalar() instead of scalars().
## Update A Particular Record By Query
```
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 
```
## Update A Record By PRIMARY KEY
```
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
```  
Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated
## Delete A Particular Record By PRIMARY KEY
```
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
```
You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.

> Dr. Angela Yu <br>
> Instructor
