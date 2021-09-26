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

@app.route('/register')
def Register():
    return render_template('./account/register.html')

@app.route('/login')
def Login():
    return render_template('./account/login.html')

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
    # return jsonify(Origin=request.headers.get('X-Forwarded-For', request.remote_addr))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8000)