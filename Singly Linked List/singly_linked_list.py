# Jacobus Burger (2022)
# Singly Linked List implemented in Python 3
# See:
# - https://en.wikipedia.org/wiki/Linked_list
# - 
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def copy(self):
        return Node(self.value)


class List:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def insert(self, value, index):
        node = Node(value)
        if not self.head:
            # insert at head of empty list
            self.head = node
        elif index <= 0:
            # insert at head of non-empty list
            node.next = self.head
            self.head = node
        else:
            # insert into the body/tail
            current = self.head
            for _ in range(index):
                if not current.next:
                    break
                current = current.next
            if not current.next:
                current.next = node
            else:
                temp = current.next
                current.next = node
                node.next = temp.next
                temp.next = None

    def remove(self, index):
        if self.length == 0:
            # remove from empty list
            return None
        elif index <= 0:
            # remove from head
            node = self.head
            self.head = self.head.next
            node.next = None
            self.length -= 1
            return node
        elif index > self.length - 1:
            # remove from tail
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            node = prev.next
            prev.next = None
            self.length -= 1
            return node
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
