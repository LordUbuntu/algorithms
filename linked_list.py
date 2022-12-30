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
    def __init__(self, *nodes: type[Node]):
        self.head = nodes[0] if len(nodes) > 0 else None
        self.tail = self.head
        for node in nodes[1:]:
            self.tail.next = node
            self.tail = self.tail.next


    def __iter__(self):
        visited = []  # avoid infinite loops
        node = self.head
        while node is not None:
            yield node
            if node in visited:
                break
            visited.append(node)
            node = node.next


    def __len__(self):
        for index, node in enumerate(self):
            if node is self.tail:
                return index + 1


    def __repr__(self):
        return ' => '.join(map(str, self))


    def __contains__(self, item):
        for node in self:
            if node is item:
                return True
        return False


    # push element to start of list (new head)
    def push(self, node):
        node = Node(node.value)
        node.next = self.head
        self.head = node


    # pop element off end of list (new tail)
    def pop(self):
        for node in self:
            if node.next is self.tail:
                result = Node(self.tail.value)
                node.next = None
                self.tail = node
                return result


    # add elements to end of list
    def append(self, *nodes):
        for node in nodes:
            self.tail.next = node
            self.tail = self.tail.next


    # adds  the elements of a LinkedList onto this list
    def extend(self, List):
        for node in List:
            self.tail.next = node
            self.tail = self.tail.next


    # remove elements from end of list
    def remove(self, amount):
        for _ in range(amount):
            self.pop()


    # count number of occurences of a given value
    def count(self, value):
        total = 0
        for node in self:
            total += 1 if node.value == value else 0
        return total


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
