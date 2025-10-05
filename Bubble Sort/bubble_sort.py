# Jacobus Burger (2022)
# Bubble Sort (Python 3)
# Bubble Sort is a straightforwards sorting algorithm and often the first
#   taught in Compting Science courses. It's time complexity of O(n^2)
#   is "bad" on large arrays, but it's simple design makes it
#   straightforward to implement and effective to use on smaller
#   arrays. Overall, it's a decent if inefficient sorting algorithm!
# see:
# - https://en.wikipedia.org/wiki/Bubble_sort
# - https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#Python
from random import randint


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sort(array: list) -> list:
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                unsorted = True


if __name__ == "__main__":
    # get input
    n = int(input())
    array = [randint(0, n) for _ in range(n)]

    # show unsorted
    # NOTE: cool snakelang trick to avoid looping when printing a list
    print(*array, sep=' ')

    # sort
    sort(array)

    # show sorted
    print(*array, sep=' ')
