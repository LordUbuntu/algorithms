# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice
import operator as op
from functools import total_ordering




@total_ordering
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


    def __repr__(self):
        return str(self.value)


    def __lt__(self, other):
        return self.value < other.value


    def __eq__(self, other):
        return self.value == other.value


    def copy(self):
        return Node(self.value)


class LinkedList(Node):
    pass


class DoublyLinkedList(Node):
    pass
