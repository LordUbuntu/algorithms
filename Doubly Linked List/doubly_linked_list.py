# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice
from functools import total_ordering



@total_ordering
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def copy(self):
        return Node(self.value)


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass
