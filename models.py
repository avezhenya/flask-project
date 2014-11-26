from app import app
from flask.ext.sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#create sqlalchemy object
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
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

    #relationshop
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))

    def __init__(self, name, year, autor_id):
        self.name = name
        self.year = year
        self.autor_id = autor_id

    def __repr__(self):
        return '<Book is %r, year is %r, autor is %r>' % (self.name, self.year, self.autor_id)


class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    #autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name is %r >' % self.name