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


class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        for value in values:
            # set head and tail to first Node
            if self.head is None:
                self.head = Node(value)
                self.tail = self.head
                continue
            # append every subsequent Node
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


class DoublyLinkedList(Node):
    pass
