from flask import Flask,render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import re

import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'TIGER'

app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6434890'
app.config['MYSQL_PASSWORD'] = 'QS9iTpVBGM'
app.config['MYSQL_DB'] = 'sql6434890'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = 'Please enter your username and password'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account1 WHERE username = %s AND password = %s', (username, password,))
        acc = cursor.fetchone()
        if acc:
            session['loggedin'] = True
            session['id'] = acc['id']
            session['username'] = acc['username']
            return redirect(url_for('userhome'))
        else:
            msg = 'Incorrect username or password!'
    return render_template('signin.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = 'Sign up!'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account1 WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO account1 VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route("/home")
def userhome():
    if 'loggedin' in session:
        username=session.get("username")
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM books ')
        value = cursor.fetchall() 
        print(value)
        return render_template('home.html', books=value,username=username)

@app.route("/session")  
def sess():
    username=session.get("username")
    return username

@app.route("/navbar")  
def nav():
    return render_template('navbar.html')    


if __name__=="__main__":
    app.run(debug=True);  