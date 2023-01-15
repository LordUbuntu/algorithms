# Jacobus Burger (2023)
# Practice implementing a binary tree (bifurcating arborescence)
# See https://en.wikipedia.org/wiki/Binary_tree


# recursive node based tree
class BinaryNodeTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
