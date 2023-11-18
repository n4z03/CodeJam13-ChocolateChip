import heapq

class NotificationHeap:
    def __init__(self):
        self.queue = []
    
    def __init__(self, filepath):
        pass

    def add(self, date_object):
        heapq.heappush(self.queue, date_object)

    def pop_oldest(self):
        if self.queue:
            return heapq.heappop(self.queue)
        raise IndexError("pop from empty DateQueue")

    def __repr__(self):
        return f"DateQueue({self.queue})"