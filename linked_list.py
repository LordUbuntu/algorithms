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





class ListIterator:
    def __iter__(self):
        # we have to avoid loops
        hare = self.head

        # iterate through all nodes
        node = self.head  # the "turtle"
        while node is not None:
            yield node
            node = node.next

            # manage loops
            if hare is not None and hare.next is not None:
                hare = hare.next.next
                if node is hare:
                    yield node
                    break


    def __len__(self):
        for index, node in enumerate(self):
            if node is self.tail:
                return index + 1


    def __contains__(self, item):
        for node in self:
            if node is item:
                return True
        return False


    # count number of occurences of a given value
    def count(self, value):
        total = 0
        for node in self:
            total += 1 if node.value == value else 0
        return total





class SinglyLinkedList(ListIterator):
    def __init__(self, *nodes: type[Node]):
        self.head = nodes[0] if len(nodes) > 0 else None
        self.tail = self.head
        for node in nodes[1:]:
            self.tail.next = node
            self.tail = self.tail.next


    def __repr__(self):
        cycle = " (cycle)" if self.has_cycle() else ''
        return ' => '.join(map(str, self)) + cycle


    def copy(self):
        return SinglyLinkedList(*[node.copy() for node in self])


    def insert(self, index, node):
        i = 0
        for current in self:
            if i == index - 1:
                node.next = current.next
                current.next = node
                break


    def remove(self, index):
        i = 0
        for current in self:
            if i == index - 1:
                node = current.next
                current.next = node.next
                node.next = None
                return node
            i += 1


    # reverse the linked list in place using DFS
    def reverse(self):
        # traverse down list
        visited = []
        visited.extend(node for node in self)

        # set last element as first
        self.head = visited.pop()
        self.tail = self.head
        
        # visit and link nodes in reverse order
        for _ in range(len(visited)):
            self.tail.next = visited.pop()
            self.tail = self.tail.next
        self.tail.next = None


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





class DoublyLinkedList(ListIterator):
    # doubly linked list
    def __init__(self, *nodes: type[Node]):
        self.head = nodes[0] if len(nodes) > 0 else None
        self.tail = self.head
        for node in nodes[1:]:
            self.tail.next = node
            prev = self.tail
            self.tail = self.tail.next
            self.tail.prev = prev


    def __repr__(self):
        cycle = " (cycle)" if self.has_cycle() else ''
        return ' <=> '.join(map(str, self)) + cycle


    def copy(self):
        return DoublyLinkedList(*[node.copy() for node in self])


    def insert(self, index, node):
        i = 0
        for current in self:
            if i == index - 1:
                # attach target node to list
                node.next = current.next
                node.next.prev = node
                # attach current node to target node
                node.prev = current
                current.next = node
                # done
                break


    def remove(self, index):
        i = 0
        for current in self:
            if i == index - 1:
                # detach current node from target node
                node = current.next
                current.next = current.next.next
                current.next.prev = current
                # detach target node from list
                node.next = None
                node.prev = None
                break


    # reverse the doubly linked list in place by swapping prev and next
    def reverse(self):
        # forall nodes swap next and prev direction
        node = self.head
        while node is not None:
            node.next, node.prev = node.prev, node.next
            node = node.prev
        # swap head and tail
        self.head, self.tail = self.tail, self.head


    # Floyd's algorithm (checking both ways)
    def has_cycle(self):
        # check forwards
        if SinglyLinkedList.has_cycle(self):
            return True
        # check backwards
        turtle = self.tail
        hare = self.tail
        while turtle is not None \
                and hare is not None \
                and hare.prev is not None:
            turtle = turtle.prev
            hare = hare.prev.prev
            if turtle is hare:
                return True
        return False
