# Jacobus Burger (2023)
# Practice implementing a binary heap tree (array representation)
from math import ceil, floor, log


class BinaryHeapTree:
    def __init__(self, *data):
        if len(data) > 0:
            # create a complete tree of 2**h nodes
            self.height = ceil(log(len(data)) / log(2))
            self.tree = [
                data[i]
                if i < len(data)
                else None
                for i in range(2**self.height)
            ]
        else:
            self.height = 1
            self.tree = [None]


    def __repr__(self):
        return ' '.join(map(str, self.tree))


    def parent(self, index):
        return floor((index - 1) / 2)


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2


    def preorder(self):
        pass
