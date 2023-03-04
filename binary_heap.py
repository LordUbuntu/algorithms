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
        index = None
        while stack:
            v = stack.pop()
            if self.tree[v] is None:
                self.tree[v] = data
                index = v
                break
            visited.append(v)
            if self.right(v) < len(self.tree):
                stack.append(self.right(v))
            if self.left(v) < len(self.tree):
                stack.append(self.left(v))
        # rebalance tree (parent <= children)
        while index != 0 and self.tree[self.parent(index)] > self.tree[index]:
            temp = self.tree[index]
            self.tree[index] = self.tree[self.parent(index)]
            self.tree[self.parent(index)] = temp
            index = self.parent(index)


    def remove(self):
        # grab smalest item in heap (root)
        result = self.tree[0]
        # end early if only root element in tree:
        if len(self.tree) == 1 or all(node is None for node in self.tree[1:]):
            self.tree[0] = None
            return result
        # replace root with most recent child (first valid on end of list)
        for index, value in enumerate(reversed(self.tree)):
            if value is not None:
                self.tree[0] = value
                self.tree[index] = None
                break
        # rebalance tree
        index = 0
        while self.tree[index] > self.tree[self.left(index)] or self.tree[index] > self.tree[self.right(index)]:
            left = self.left(index)
            right = self.right(index)
            if self.tree[left] > self.tree[index] and self.tree[left] is not None:
                # swap left
                temp = self.tree[left]
                self.tree[left] = self.tree[index]
                self.tree[index] = temp
                # follow
                index = left
            elif self.tree[right] > self.tree[index] and self.tree[right] is not None:
                # swap right
                temp = self.tree[right]
                self.tree[right] = self.tree[index]
                self.tree[index] = temp
                # follow
                index = right
            elif self.tree[left] <= self.tree[index] and self.tree[right] <= self.tree[index]:
                # tree is balnced, end rebalancing
                break
            # don't continue if next indices are None value or out of bounds
            if self.left(left) >= len(self.tree) or self.right(right) >= len(self.tree) or index >= len(self.tree):
                break
            if self.tree[self.left(left)] is None or self.tree[self.right(right)] is None:
                break
        return result
