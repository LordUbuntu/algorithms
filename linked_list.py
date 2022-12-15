# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice



class List:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


    def __str__(self):
        return ' => '.join([str(node.value) for node in self])


    def __eq__(self, other):
        if len(self) == len(other):
            return all([a.value == b.value for a, b in zip(self, other)])
        return False


    def __len__(self):
        for index, node in enumerate(self):
            if node.next is None:
                return index + 1


    def __iter__(self):
        current = self
        while current.next is not None:
            yield current
            current = current.next
        yield current


    def head(self):
        return self


    def tail(self):
        current = self
        while current.next is not None:
            current = current.next
        return current


    def contains(self, value):
        return any([current.value == value for current in self])


    def index(self, value):
        for index, current in enumerate(self):
            if current.value == value:
                return index
        return -1


    def add(self, *values):
        current = self.tail()
        for value in values:
            current.next = List(value)
            current = current.next


    def append(self, other):
        self.tail().next = other


    def insert(self, index, value):
        if index == 0:
            next = List(self.value, self.next)
            self.value, self.next = value, next
        elif index > 0:
            current = self
            for _ in range(index - 1):
                current = current.next
            current.next = List(value, current.next)


    def pop(self):
        current = self
        # return value and destroy list if only 1 node exists
        if current.next is None:
            return value
        # return value of last element in list otherwise
        while current.next is not None:
            if current.next.next is None:
                node = current.next
                value = node.value
                current.next = node.next
                del(node)
                return value
            current = current.next


    def take(self, n):
        result = List(self.value)
        current = self
        for _ in range(n):
            current = current.next
            result.add(current.value)
        return result


    def remove_all(self, value):
        current = self
        while current.next is not None:
            if current.next.value is value:
                node = current.next
                current.next = current.next.next
                del(node)
            else:
                current = current.next


    def remove(self, value):
        current = self
        while current.next is not None:
            if current.next.value is value:
                node = current.next
                current.next = current.next.next
                del(node)
                break
            current = current.next













class DoubleList:
    # doubly linked list
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


    def __str__(self):
        return ' => '.join([str(node.value) for node in self])


    def __eq__(self, other):
        if len(self) == len(other):
            return all([a.value == b.value for a, b in zip(self, other)])
        return False


    def __len__(self):
        for index, node in enumerate(self):
            if node.next is None:
                return index + 1
