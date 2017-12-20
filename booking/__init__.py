from flask import Flask
from config import Config
# from flask_pymongo import PyMongo
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

from booking import routes, models