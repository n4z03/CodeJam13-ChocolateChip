import heapq
from src.Notification import Notification

from src.SendEmail import update_email_html, send_email
from datetime import datetime

existing = set()

class NotificationQueue:
    def __init__(self):
        self.heap = []
    
    def add_notification(self, notification = Notification):
        heapq.heappush(self.heap, notification)
        existing.add(notification)

    def exists(self, notification):
        return notification in existing

    def process_notifications(self):
        current_date = datetime.now()
        while self.heap and self.heap[0].date <= current_date:
            notification = heapq.heappop(self.heap)
            update_email_html(notification)
            send_email(0) #session.user.email
        heapq.heapify(self.heap)

    def modify_notification(self, notification, new_date):
        # Modify the date of a notification and reheapify
        if notification in self.heap:
            notification.modify(new_date)
            heapq.heapify(self.heap)

# Create the queue

# Example: Adding notifications


# Process notifications (this would be called periodically, e.g., every day)
if __name__ == "__main__":
    notification_queue = NotificationQueue()
    # load notification queue from database
    # upload notification queue
    # 