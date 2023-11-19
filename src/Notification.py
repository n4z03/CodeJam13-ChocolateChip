from datetime import datetime, timedelta

class Notification:
    def __init__(self, ):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.user = user_object
        self.cookie_object = cookie_object
        

    def __repr__(self):
        return f"Notification:({self.date.strftime('%Y-%m-%d')}, to {self.chip_object.name})"

    def __lt__(self, other):
        return self.date < other.date
        
    def modify(self, date):
        self.date = date

class DateIncrement:
    def __init__(self, days, weeks, months):
        self.days = days
        self.weeks = weeks
        self.months = months
    def increment(self, date = datetime):
        days_increment = self.weeks * 7 + self.months * 30 + self.days
        date += timedelta(days = days_increment)
        return date
        
if __name__ == "__main__":
    curr_date = datetime.now()
    date_increment = DateIncrement(20, 1, 1)
    curr_date = date_increment.increment(curr_date)
    print(curr_date)

