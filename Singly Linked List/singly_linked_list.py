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

    def __str__(self):
        return str(self.value)

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
        return " -> ".join([str(node) for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
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
                if not current.next.next:
                    break
                current = current.next
            next = current.next
            current.next = next.next
            next.next = None
            return next

    def find(self, value):
        # don't search empty lists
        if not self.head:
            return -1
        # search non-empty list
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def peek(self, index):
        # don't peek empty list
        if not self.head:
            return None
        else:
            current = self.head
            i = 0
            while current:
                if (i == index):
                    return current.value
                current = current.next
                i += 1
            return None


if __name__ == "__main__":
    if len(argv) < 2:
        exit(1)
    list = List()

    print("start")
    print(list.head)
    print(list)

    print("insert nodes:")
    for i in range(1, len(argv)):
        list.insert(int(argv[i]), 0)
    print(list)

    print("search for node with value 13: {}".format(list.find(13)))

    print("value of node at index 2: {}".format(list.peek(2)))

    print("remove from head:")
    print("value: {}".format(list.remove(-1)))
    print(list)

    print("remove from tail:")
    print("value: {}".format(list.remove(1)))
    print(list)

    print("remove from end:")
    print("value: {}".format(list.remove(1_000_000)))
    print(list)

    print("removing all nodes:")
    while list.head:
        print(list)
        print("  {}".format(list.remove(0)))

    print("remove from empty list:")
    list.remove(-1)
    list.remove(1)
    print(list)
