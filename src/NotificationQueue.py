import heapq
import Notification
import SendEmail
from datetime import datetime

class NotificationQueue:
    def __init__(self):
        self.heap = []

    def __init__(self, filepath):
        self.heap = []

    def add_notification(self, notification = Notification):
        heapq.heappush(self.heap, notification)

    def process_notifications(self):
        current_date = datetime.now()
        while self.heap and self.heap[0].date <= current_date:
            notification = heapq.heappop(self.heap)
            SendEmail.send_email(notification.user.email)
        heapq.heapify(self.heap)

    def modify_notification(self, notification, new_date):
        # Modify the date of a notification and reheapify
        if notification in self.heap:
            notification.modify(new_date)
            heapq.heapify(self.heap)

# Create the queue
notification_queue = NotificationQueue()

# Example: Adding notifications
notification_queue.add_notification(Notification("2023-11-20", user_obj, cookie_obj, chip_obj))
notification_queue.add_notification(Notification("2023-11-25", user_obj, cookie_obj, chip_obj))

# Process notifications (this would be called periodically, e.g., every day)
notification_queue.process_notifications(send_email)