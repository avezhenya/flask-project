from flask import Flask, render_template, url_for, request, redirect, session, flash
from functools import wraps
from models import *

#create application object
app = Flask(__name__)
app.secret_key = 'random'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def index():
    books = db.session.query(Book).all()
    print books
    return render_template('index.html', books=books)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Incorrect username or password. Please try again!'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)