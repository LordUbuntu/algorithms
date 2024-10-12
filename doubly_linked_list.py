# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice
import operator as op
from functools import total_ordering



# total ordering was used because I am lazy :)
@total_ordering
class Node:
    def __init__(self, value=None):
        # I include both next and prev for singly and doubly linked list
        # implementations, but I could just as well have a list of reference nodes
        # for a more generic graph (where each vertex can have n edges). Because
        # linked lists are a linear directed graph which is a subset of a more
        # general graph.
        self.value = value
        self.next = None
        self.prev = None

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def copy(self):
        return Node(self.value)


# A linked list is composed of Nodes, so it does not inherit from a Node base class
# composition over inheritence
# It's possible to implement singly and doubly linked lists recursively
# I decided to implement just a doubly linked list since it's an extension of the
# singly linked list and has broader applications. The difference only involves
# anywhere where prev is used
class DoublyLinkedList:
    # A karg of values of any type are taken instead of a karg of Nodes to make it
    # much easier to simply initialize a long linked list of generic values.
    def __init__(self):
        # head and tail are initially both None because the simplest linked list
        # graph is an empty one, and from there the initial node and all subsequent
        # nodes can be constructed
        self.head = None
        self.tail = None
        self.length = 0
    
    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert(self, value, index):
        if index <= 0:
            # insert into the head
            self.insert_head(value)
        if index >= len(self) - 1:
            # insert into the tail
            self.insert_tail(value)
        else:
            # insert into the spine/body
            current = self.head
            for _ in range(index):
                current = current.next
            node = Node(value)
            node.next = current.next
            node.prev = current
            current.next = node

    def pop(self):
        node = self.head
        self.head = self.head.next
        node.next = None
        return node

    def truncate(self):
        node = self.tail
        self.tail = self.tail.prev
        node.prev = None
        return node

    def remove(self, index):
        if index <= 0:
            # remove from head
            return self.pop()
        elif index >= len(self) - 1:
            # remove from tail
            return self.truncate()
        else:
            # remove from spine/body
            current = self.head
            for _ in range(index):
                current = current.next
            node = current
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            return node

    # I implemeted as O(n) because that's how I remember the length function operating,
    # but you could just as well add a single variable to remember the length and
    # update it whenever you insert or remove values, then the time complexity and
    # space complexity both become O(1), which is far better
    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count
