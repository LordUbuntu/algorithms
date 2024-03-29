# Jacobus Burger (2023)
# A binary heap tree (array representation)
# See https://en.wikipedia.org/wiki/Binary_heap
#     https://www.youtube.com/watch?v=AE5I0xACpZs
from math import ceil, log
from collections import deque


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
        tree = self.tree
        result = ""
        for i in range(self.height):
            result += ' '.join(map(str, tree[:2**i])) + '\n'
            tree = tree[2**i:]
        return result


    # generates values in the tree based on traversal order generator
    def gen(self, generator):
        return [self.tree[i] for i in generator()]


    def parent(self, index):
        return (index - 1) // 2


    def left(self, index):
        return 2 * index + 1


    def right(self, index):
        return 2 * index + 2


    # generate indices in DFS preorder
    # noticed that this pattern appears a lot. So I made it a generator
    #   so that it could be used elsewhere.
    def preorder(self):
        visited, stack = [], [0]
        while stack:
            v = stack.pop()
            if self.tree[v] is None:
                continue
            yield v
            visited.append(v)
            # note: right comes before left, FILO stack
            if self.right(v) < len(self.tree):
                stack.append(self.right(v))
            if self.left(v) < len(self.tree):
                stack.append(self.left(v))


    # generate indices in BFS levelorder
    # noticed that this pattern appears a lot. So I made it a generator
    #   so that it could be used elsewhere.
    def levelorder(self):
        visited, queue = [], deque([0])
        while queue:
            v = queue.popleft()
            if self.tree[v] is None:
                continue
            yield v
            visited.append(v)
            # note: left comes before right, FIFO queue
            if self.left(v) < len(self.tree):
                queue.append(self.left(v))
            if self.right(v) < len(self.tree):
                queue.append(self.right(v))





class MinHeap(BinaryHeapTree):
    def __init__(self, *data):
        super().__init__(*data)


    def insert(self, data):
        # extend array to include a new level of tree
        if all(node is not None for node in self.tree):
            self.height += 1
            self.tree.extend([None] * (2**self.height - 2**(self.height-1)))
        # put item in first available space
        index = -1
        for v in self.preorder():
            if self.tree[v] is None:
                self.tree[v] = data
                index = v
                break
        # bubble up to satisfy heap invariant
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
        # replace root with most recent child (first valid from end of list)
        for index in range(len(self.tree) - 1, -1, -1):
            if self.tree[index] is not None:
                self.tree[0] = self.tree[index]
                self.tree[index] = None
                break
        # bubble up to satisfy heap invariant
        smallest = index = 0
        left = self.left(index)
        right = self.right(index)
        while left < len(self.tree) and right < len(self.tree):
            if self.tree[smallest] is None:
                break
            if self.tree[left] is not None \
                    and self.tree[left] < self.tree[smallest]:
                smallest = left
            if self.tree[right] is not None \
                    and self.tree[right] < self.tree[smallest]:
                smallest = right
            if smallest != index:
                temp = self.tree[smallest]
                self.tree[smallest] = self.tree[index]
                self.tree[index] = temp
            else:
                break
            index = smallest
            left = self.left(index)
            right = self.right(index)
        # return result
        return result


    def search(self, data):
        # DFS for first occurence of value
        for v in self.preorder():
            if self.tree[v] == data:
                return v





class MaxHeap(BinaryHeapTree):
    def __init__(self, *data):
        super().__init__(*data)


    def insert(self, data):
        # make more space if tree is complete (add new level)
        if all(node is not None for node in self.tree):
            self.height += 1
            self.tree.extend([None] * (2**self.height - 2**(self.height-1)))
        # put item in first available space
        index = -1
        for v in self.preorder():
            if self.tree[v] is None:
                self.tree[v] = data
                index = v
                break
        # bubble up to satisfy heap invariant
        while index != 0 and self.tree[self.parent(index)] < self.tree[index]:
            temp = self.tree[index]
            self.tree[index] = self.tree[self.parent(index)]
            self.tree[self.parent(index)] = temp
            index = self.parent(index)


    def search(self, data):
        # DFS for first occurence of value
        for v in self.preorder():
            if self.tree[v] == data:
                return v
