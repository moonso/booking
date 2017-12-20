import datetime

from booking import (login, app)
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash, check_password_hash)

class User(UserMixin, dict):
    """User class for mongdb"""
    def __init__(self, username, email=None, password_hash=None):
        """
        Args:
            username(str)
            email(str)
            password_hash(str)
        """
        super(User, self).__init__()
        self.username = username
        self.email = email
        self.password_hash = password_hash
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Bill(dict):
    """Represent billing information"""
    def __init__(self, amount, category, company, user_id):
        super(Bill, self).__init__()
        self.amount = amount
        self.category = category
        self.company = company
        self.user_id = user_id
        self.timestamp = datetime.datetime.now()
        
    def __repr__(self):
        return '<Bill({0}:{1}:{2}>'.format(
                self.company, self.amount, self,category)

@login.user_loader
def user_loader(username):
    user_obj = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not user_obj:
        return None
    return User(user_obj['_id'], user_obj['email'], user_obj['password_hash'])
    