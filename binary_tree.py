# Jacobus Burger (2023)
# Info:
#   Very basic implementation of a binary tree.


# All subtrees are trees, ergo recursive definition
class BTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right





# my preferred solution: a binary heap tree
from math import ceil, floor, log
class HeapTree:
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


    def parent(self):
        if self.index > 0:
            self.index = floor((self.index - 1) / 2)


    def left(self):
        self.index = 2 * self.index + 1


    def right(self):
        self.index = 2 * self.index + 2
