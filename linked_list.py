# Jacobus Burger (2022)
# Linked List implementation in Python for fun and practice

class List:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return self.value is other.value

    def add(self, value):
        current = self
        while current.next is not None:
            current = current.next
        current.next = List(value)

    def remove(self, value):
        current = self
        while current.next is not None:
            if current.next.value is value:
                node = current.next
                current.next = current.next.next
                del(node)
                break
            current = current.next

    def insert(self, index, value):
        current = self
        if index == 0:
            temp = current
            current = List(value, temp)
        else:
            for _ in range(index - 1):
                if current.next is not None:
                    current = current.next
            current.next = List(value, current.next)

    def show(self):
        current = self
        while current.next is not None:
            print(f"{current.value} => ", end="")
            current = current.next
        print(f"{current.value}")
