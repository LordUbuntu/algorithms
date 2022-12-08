# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice

class List:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


    def __str__(self):
        return f"{self.value}"


    def __eq__(self, other):
        if len(self) == len(other):
            return all([a.value == b.value for a, b in zip(self, other)])
        return False


    def __len__(self):
        length = 0
        current = self
        while current.next is not None:
            current, length = current.next, length + 1
        return length + 1


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
        return any([current.value == node.value for current in self])


    def index(self, value):
        for index, current in enumerate(self):
            if current.value == value:
                return index
        return -1


    def add(self, value):
        current = self.tail()
        current.next = List(value)


    def append(self, other):
        current = self.tail()
        current.next = other


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
            value, self.value = self.value, None
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


    def show(self):
        return " => ".join(map(str, self))
