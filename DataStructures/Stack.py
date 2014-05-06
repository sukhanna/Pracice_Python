__author__ = 'Sumeet'

class Stack:

    # constructor
    def __init__(self):
        self.items = []

    # returns and removes top most element of stack and modifies the stack
    def pop(self):
        return self.items.pop()

    # returns top most element of the stack without modifying the stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # pushes the element into the stack from top
    def push(self, element):
        self.items.append(element)

    # returns number of elements in stack
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0