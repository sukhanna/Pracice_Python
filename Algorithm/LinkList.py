__author__ = 'sukhanna'
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next;

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data



class List:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def get_first(self):
        return self.head

    def insert(self, item, index):
        previous = current = self.get_first()
        item_index = 0
        found = False
        while current is not None and not found:
            if index == 0:
                temp = self.head
                new_node = Node(item)
                new_node.next = temp
                self.head = new_node
                found = True
            elif item_index == index:
                temp = previous.next
                new_node = Node(item)
                new_node.next = temp
                previous.next = new_node
                found = True

            item_index += 1
            previous = current
            current = current.get_next()

    def printList(self):
        # print all the items
        n = self.get_first()
        while n is not None:
            print(n.data)
            n = n.get_next()