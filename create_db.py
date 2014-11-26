from models import db, User, Autor, Book

db.drop_all()
db.create_all()

a = User('admin', 'admin')
db.session.add(a)

c = Autor('Pushkin A.S.')
b = Book('War and freedom', '1874', 1)

db.session.add(c)
db.session.add(b)
db.session.add(Book('Math 6 klass', '2013', 2))
db.session.add(Book('English 8 klass', '2011', 3))

db.session.commit()

print User.query.all()
print Book.query.all()
print Autor.query.all()