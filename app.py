from flask import Flask,render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'TIGER'

app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6434890'
app.config['MYSQL_PASSWORD'] = 'QS9iTpVBGM'
app.config['MYSQL_DB'] = 'sql6434890'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True);  