__author__ = 'sukhanna'

# queue implementation - FIFO
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


