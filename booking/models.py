import datetime

class User(dict):
    """User class for mongdb"""
    def __init__(self, username, email=None, password_hash=None):
        """
        Args:
            username(str)
            email(str)
            password_hash(str)
        """
        super(User, self).__init__()
        self['username'] = username
        self['email'] = email
        self['password_hash'] = password_hash
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Bill(dict):
    """Represent billing information"""
    def __init__(self, amount, category, company, user):
        super(Bill, self).__init__()
        self['amount'] = amount
        self['category'] = category
        self['company'] = company
        self['user'] = user
        self['timestamp'] = datetime.datetime.now()
        
    def __repr__(self):
        return '<Bill({0}:{1}:{2}>'.format(
                self.company, self.amount, self,category)

        