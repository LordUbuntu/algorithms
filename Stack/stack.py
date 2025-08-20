# Jacobus Burger (2025-08-18)
# Stack (Python 3)
# Description:
# Stacks are a First In Last Out (FILO) data structure where you can
#      `push` items to the top, or `pop` items from the top, like adding
#      and removing sheets of paper from the top of a stack of paper.
# Info:
# - https://en.wikipedia.org/wiki/Stack_(abstract_data_type)


# Stack Abstract Data Type (ADT)
# head: top of stack index (and size of stack)
# data: array of data (static data for now)
class Stack:
    def __init__(self, head: int = 0, data: list = []) -> None:
        self.data = data  # Python 3 lists are dynamic arrays

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, value: int) -> None:
        self.data.append(value)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self) -> int:
        if len(self.data) <= 0:
            return -1
        return self.data.pop()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
