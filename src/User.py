class User:
    def __init__(self, username, email, password):
        self.chips = []
        self.username = username
        self.email = email
        self.password = password

    def add_chip(self, chip):
        self.chips.add(chip)

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"

