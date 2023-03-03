# Jacobus Burger (2023)
# A binary heap tree (array representation)
# See https://en.wikipedia.org/wiki/Binary_heap
from math import ceil, log


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
        return (index - 1) // 2


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2


    def preorder(self):
        # navigate by index
        visited, stack = [], [0]
        # result by value
        result = []
        while stack:
            v = stack.pop()
            if self.tree[v] is None:
                continue
            visited.append(v)
            result.append(self.tree[v])
            if self.right(v) < len(self.tree):
                stack.append(self.right(v))
            if self.left(v) < len(self.tree):
                stack.append(self.left(v))
        return result


class MinHeap(BinaryHeapTree):
    def __init__(self, *data):
        super().__init__(*data)


    def insert(self, data):
        # grow array if no more room
        if all(node is not None for node in self.tree):
            self.height += 1
            self.tree.extend([None] * (2**self.height - 2**(self.height-1)))
        # put item in first available space
        visited, stack = [], [0]
        node = None
        while stack:
            v = stack.pop()
            if self.tree[v] is None:
                self.tree[v] = data
                node = v
                break
            visited.append(v)
            if self.right(v) < len(self.tree):
                stack.append(self.right(v))
            if self.left(v) < len(self.tree):
                stack.append(self.left(v))
        # rebalance tree (parent <= children)
        while node != 0 and self.tree[self.parent(node)] > self.tree[node]:
            temp = self.tree[node]
            self.tree[node] = self.tree[self.parent(node)]
            self.tree[self.parent(node)] = temp
            node = self.parent(node)


    def remove(self):
        return self.tree.pop(0)
