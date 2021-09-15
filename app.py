from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask.wrappers import Request
from flask_mysqldb import MySQL
from werkzeug.local import F
import hashlib

# MySql Connection
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='perikosdb'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 7000, debug = True)