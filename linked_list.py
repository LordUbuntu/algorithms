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
class LinkedList:
    # A karg of values of any type are taken instead of a karg of Nodes to make it
    # much easier to simply initialize a long linked list of generic values.
    def __init__(self, *values):
        # head and tail are initially both None because the simplest linked list
        # graph is an empty one, and from there the initial node and all subsequent
        # nodes can be constructed
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

    # iteration is simple. I start at the head, and then for every node I just yeild
    # the current one and then go to the next one, until I reach the end of the
    # linked list.
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


class DoublyLinkedList(Node):
    pass
