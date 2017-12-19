import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_DBNAME = 'flask-test'
    MONGO_URI = "mongodb://flask:hello@ds159676.mlab.com:59676/flask-test"