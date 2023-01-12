# Jacobus Burger (2023)
# Info:
#   Practice implementing a binary tree


# recursive node based tree
class BinaryNodeTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right





# my preferred solution: a binary heap tree
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
        return str(self.tree)


    def parent(self, index):
        return floor((index - 1) / 2)


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2


    def preorder(self):
        visited = []
        index = 0
        root = self.tree[index]
        while root not in visited:
            # go left if possible
            if self.tree[self.left(index)] not in visited \
                    and self.tree[self.left(index)] is not None:
                index = self.left(index)
            # else go right if possible
            elif self.tree[self.right(index)] not in visited \
                    and self.tree[self.right(index)] is not None:
                index = self.right(index)
            # otherwise record node as visited and return to parent
            else:
                visited.append(self.tree[index])
                index = self.parent(index)

