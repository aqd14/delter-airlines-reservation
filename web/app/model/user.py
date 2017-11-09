# app/model/user.py

class User(object):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
