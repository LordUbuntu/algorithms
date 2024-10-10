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
class LinkedList:
    # A karg of values of any type are taken instead of a karg of Nodes to make it
    # much easier to simply initialize a long linked list of generic values.
    def __init__(self):
        # head and tail are initially both None because the simplest linked list
        # graph is an empty one, and from there the initial node and all subsequent
        # nodes can be constructed
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        self.tail.next = Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    # decided that if index exceeds length of linked list, that it should always just
    # append to the end, and if an index before list, then insert at head
    def insert(self, value, index):
        # insert the head of the linked list
        if index <= 0:
            self.insert_head(value)
        else:
            current = self.head
            for _ in range(index - 1):
                # insert into the tail of the linked list
                if current == self.tail:
                    self.insert_tail(value)
                current = current.next
            # insert into the spine of the linked list
            else:
                node = Node(value)
                node.next = current.next
                node.prev = current
                current.next = node

    def remove(self, index):
        pass

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
