# Jacobus Burger (2023)
# Info:
#   Very basic implementation of a binary tree.


# All subtrees are trees, ergo recursive definition
class BTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
