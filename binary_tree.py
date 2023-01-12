# Jacobus Burger (2023)
# Info:
#   Very basic implementation of a binary tree.


# recursive node based tree
class BinaryNodeTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def left(self):
        return self.left


    def right(self):
        return self.right



# my preferred solution: a binary heap tree
from math import ceil, floor, log
class BinaryHeapTree:
    def __init__(self, *data):
        self.index = 0
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
            self.tree = [None]
            self.height = 1


    def __repr__(self):
        return str(self.tree)


    def __setitem__(self, index, item):
        self.tree[index] = item


    def __getitem__(self, index):
        return self.tree[index]


    def parent(self, index):
        return floor((index - 1) / 2)


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2
