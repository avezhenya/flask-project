#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import db, User, Author, Book

db.drop_all()
db.create_all()

a = User('admin', 'admin')
db.session.add(a)

books = [u"100 лет одиночества", u"Колыбель для кошки", u"Прощай оружие",
     u"Повелитель мух", u"Чапаев и пустота", u"Бойцовский клуб", u"451 градус по Фаренгейту"]
authors = [u"Габриэль Гарсия Маркес", u"Курт Воннегут", u"Эрнест Хемингуэй",
     u"Уильям Голдинг", u"Виктор Пелевин", u"Чак Паланик", u"Рэй Дуглас Брэдбери"]
years = [1967, 1980, 1945, 1954, 1996, 1996, 1953]

for i in range(len(years)):
    db.session.add(Author(authors[i]))
    y = Author.query.get(i+1).id
    db.session.add(Book(books[i], years[i], y))

db.session.commit()