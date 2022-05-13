from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#want to incrypt our password using hashing function
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
#in order to make the falsk to understand that this is a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rate.db'  #this is a dictionary accept some new key value, dictionary with the key is SQL.. value is 'sqlite'
#convention is to use the key like above. URI is uniform resourse identifier
app.config['SECRET_KEY'] = '224a0afbee8e3989828cf8ea'
db = SQLAlchemy(app)
# this is the database you want to connect with
# this will link to the instance you create in the flask instance you

bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
# password hashing encrypt and login_manager for login

from rate import routes