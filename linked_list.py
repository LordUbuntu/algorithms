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





class LinkedList:
    def __init__(self, *values):
        self.head = Node(values[0]) if len(values) > 0 else Node()
        node = self.head
        for value in values[1:]:
            node.next = Node(value)
            node = node.next
        node.next = None
        self.tail = node


    def __len__(self):
        for index, node in enumerate(self):
            if node == self.tail:
                return index + 1


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        return ' => '.join(map(str, self))


    # push element to start of list (new head)
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


    # pop element off end of list (new tail)
    def pop(self):
        for node in self:
            if node.next is self.tail:
                result = Node(self.tail.value)
                node.next = None
                self.tail = node


    # add elements to end of list
    def append(self, *values):
        for value in values:
            self.tail.next = Node(value)
            self.tail = self.tail.next


    def remove(self, amount):
        for _ in range(amount):
            self.pop()


    # Floyd's algorithm for finding cycles
    def has_cycle(self):
        turtle = self.head
        hare = self.head
        while turtle is not None \
                and hare is not None \
                and hare.next is not None:
            turtle = turtle.next
            hare = hare.next.next
            if turtle is hare:
                return True
        return False





class DoubleList:
    # doubly linked list
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
