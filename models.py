from app import app
from flask.ext.sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#create sqlalchemy object
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(50))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<Login %r>' % self.login


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    year = db.Column(db.String(4))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __init__(self, name, year, author_id):
        self.name = name
        self.year = year
        self.author_id = author_id

    def __repr__(self):
        return '<Book is %r, year is %r, author is %r>' % (self.name, self.year, self.author_id)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    books = db.relationship('Book', backref='author', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name is %r >' % self.name