from ..app import *
class User(db.Model):
    def __init__(self, username, email, password):
        self.cookies = []
        self.username = username
        self.email = email
        self.password = password

    def add_cookie(self, cookie):
        self.cookies.append(cookie)

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"