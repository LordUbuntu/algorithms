# Jacobus Burger (2022)
# Singly Linked List implemented in Python 3
#
# See:
# - https://en.wikipedia.org/wiki/Linked_list
# - 
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
class List:
    # A karg of values of any type are taken instead of a karg of Nodes to make it
    # much easier to simply initialize a long linked list of generic values.
    def __init__(self):
        # head and tail are initially both None because the simplest linked list
        # graph is an empty one, and from there the initial node and all subsequent
        # nodes can be constructed
        self.head = None
        self.tail = None
        self.length = 0  # memoize length for O(1) time and space
    
    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def insert(self, value, index):
        if self.length == 0:
            # insert into empty list
            self.prepend(value)
        elif index <= 0:
            # insert into the head
            self.prepend(value)
        elif index > self.length - 1:
            # insert into the tail
            self.append(value)
        else:
            # insert into the spine/body
            current = self.head
            for _ in range(index):
                current = current.next
            node = Node(value)
            node.next = current.next
            current.next = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            node = self.head
            self.head = self.head.next
            node.next = None
            self.length -= 1
            return node

    def truncate(self):
        if self.length == 0:
            return None
        else:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            node = self.tail
            self.tail = prev
            self.length -= 1
            return node

    def remove(self, index):
        if self.length == 0:
            # remove from empty list
            return None
        elif index <= 0:
            # remove from head
            return self.pop()
        elif index > self.length - 1:
            # remove from tail
            return self.truncate()
        else:
            # remove from spine/body
            current = self.head
            prev = self.head
            for _ in range(index):
                prev = current
                current = current.next
            node = current
            prev.next = node.next
            node.next = None
            return node
