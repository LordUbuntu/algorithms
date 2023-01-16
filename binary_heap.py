# Jacobus Burger (2023)
# A binary heap tree (array representation)
# See https://en.wikipedia.org/wiki/Binary_heap
from math import ceil, floor, log


class BinaryHeapTree:
    def __init__(self, *data):
        # calculate height of complete tree that can fit data
        self.height = ceil(log(len(data) + 1, 2))
        # create a complete tree of 2**h - 1 nodes
        self.tree = [None] * (2**self.height - 1)
        # put data into tree if it exists
        for index, item in enumerate(data):
            self.tree[index] = item


    def __repr__(self):
        return ' '.join(map(str, self.tree))


    def parent(self, index):
        return floor((index - 1) / 2)


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2


    def preorder(self):
        visited = []
        index = 0
        while self.tree[0] not in visited:
            # visit node and return to parent if children outide tree
            if self.left(index) >= len(self.tree):
                visited.append(self.tree[index])
                index = self.parent(index)
                continue

            left = self.tree[self.left(index)]
            right = self.tree[self.right(index)]
            # if left can be visited
            if left not in visited and left is not None:
                # go left
                index = self.left(index)
            # if left can't be visited but right can be visited
            elif right not in visited and right is not None:
                # go right
                index = self.right(index)
            # if left and right have been visited
            else:
                # mark current node as visited and return to parent
                visited.append(self.tree[index])
                index = self.parent(index)
        return visited
