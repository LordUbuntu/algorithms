# Jacobus Burger (2022)
# Singly Linked List implemented in Python 3
# See:
# - https://en.wikipedia.org/wiki/Linked_list
from sys import argv
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, value):
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

    def __str__(self):
        return " -> ".join([str(node.value) for node in self])

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
                node.next = temp

    def remove(self, index):
        if not self.head:
            # remove from empty list
            return None
        elif index <= 0:
            # remove from head
            prev = self.head
            self.head = prev.next
            prev.next = None
            return prev
        else:
            # remove from body/tail
            current = self.head
            for _ in range(index):
                if not current.next:
                    break
                current = current.next
            next = current.next
            current.next = next.next
            next.next = None
            return next

    def search(self, value):
        # don't search empty lists
        if not self.head:
            return -1
        # search non-empty list
        current = self.head
        index = 0
        while self.head:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1


if __name__ == "__main__":
    if argv < 2:
        exit(1)
    for arg in argv[1:]:
        print(arg)
