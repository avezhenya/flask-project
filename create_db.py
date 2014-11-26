from models import db, User, Author, Book

db.drop_all()
db.create_all()

a = User('admin', 'admin')
db.session.add(a)

c = Author('Pushkin A.S.')
db.session.add(c)
# db.session.commit()
y = Author.query.get(1).id

b = Book('War and freedom', '1874', y)
ht = Book('Esenin',         '1827', y)

db.session.add(b)
db.session.add(ht)

db.session.commit()

print User.query.all()
print Book.query.all()
print Author.query.all()