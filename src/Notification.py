from datetime import datetime

class Notification:
    def __init__(self, date, user_object, cookie_object, chip_object):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.user = user_object
        self.cookie_object = cookie_object
        self.chip_object = chip_object

    def __repr__(self):
        return f"Notification:({self.date.strftime('%Y-%m-%d')}, to {self.chip_object.name})"

    def __lt__(self, other):
        return self.date < other.date
    
    def modify(self, date):
        self.date = date