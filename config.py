from pymongo import MongoClient
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_DBNAME = 'flask-test'

    DATABASE = MongoClient()[MONGO_DBNAME]
    
    USERS_COLLECTION = DATABASE.users
    BILLS_COLLECTION = DATABASE.bills