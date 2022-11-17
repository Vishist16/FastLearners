from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from flask_mysqldb import MySQL,MySQLdb

from . import mysql

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['email']
        password=request.form['password']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM user where username=%s AND password=%s", (username, password,))
        record = cur.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record["username"]
            return redirect(url_for('views.home'))
        else:
            msg='Incorrect username/password. Try again!'
    return render_template("tlog.html", msg=msg)

@auth.route('/logout')
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('username', None)
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.login'))
   # return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('Email must be greater than 1 characters.', category='error')
        elif password1!=password2:
            flash('Password do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            flash('Account creates!', category='success')
    return render_template("sign_up.html")