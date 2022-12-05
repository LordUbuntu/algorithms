

class List:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def add(self, node):
        current = self
        while current.next is not None:
            current = current.next
        current.next = node

    def remove(self, node):
        current = self
        while current.next is not node:
            current = current.next
        current.next = None
        del(node)

    def show(self):
        current = self
        while current.next is not None:
            print(f"{current.value} => ", end="")
            current = current.next
        print(f"{current.value}")
