# Jacobus Burger (2023)
# Practice implementing a binary tree (bifurcating arborescence)
# See https://en.wikipedia.org/wiki/Binary_tree


# recursive node based tree
class BTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data >= self.data:
            if self.right is None:
                self.right = BTree(data)
            else:
                self.right.insert(data)
        if data < self.data:
            if self.left is None:
                self.left = BTree(data)
            else:
                self.left.insert(data)
        else:
            self.data = data
