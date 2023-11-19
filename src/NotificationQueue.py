import heapq
#from app import Contact
#from src.SendEmail import update_email_html, send_email
from datetime import datetime
#from Notification import DateIncrement
import sqlite3
import time
from apscheduler.schedulers.background import BackgroundScheduler

class NotificationQueue:
    """
    def __init__(self):
        self.heap = []
        self.existing = set()
    
    def add_notification(self, notification ):
        heapq.heappush(self.heap, notification)
        self.existing.add(notification)

    def remove_notification(self, notification ):
        heapq.heappop(self.heap, notification)
        self.existing.remove(notification)

    def exists(self, notification):
        return notification in self.existing

    def process_notifications(self):
        from app import app
        with app.app_context():
            from flask import session
            current_date = datetime.now()
            while self.heap and self.heap[0].date <= current_date:
                notification = heapq.heappop(self.heap)
                update_email_html(notification)
                send_email(self['email']) 
                old_notif_date =  notification.get_date()
                date_addition = DateIncrement(int(notification.f_day), int(notification.f_week), int(notification.f_month), int(notification.f_year))
                new_notif_date = date_addition.increment(old_notif_date)
                notification.c_day = new_notif_date.day
                notification.c_month = new_notif_date.month
                notification.c_year = new_notif_date.year
                self.add_notification(notification)

            

    def modify_notification(self, notification, new_date):
        # Modify the date of a notification and reheapify
        if notification in self.heap:
            notification.modify(new_date)
            heapq.heapify(self.heap)
    """


def get_all_contacts():
    conn = sqlite3.connect('data.db') 
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM contact")

    contacts = cursor.fetchall()

    conn.close()
    return contacts

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_new_contacts, 'interval', minutes=5) 
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

    notification_queue = NotificationQueue()
