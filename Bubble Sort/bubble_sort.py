# Jacobus Burger (2022)
# Bubble Sort (Python 3)
# Bubble Sort is a straightforwards sorting algorithm and often the first
#   taught in Compting Science courses. It's time complexity of O(n^2)
#   is "bad" on large arrays, but it's simple design makes it
#   straightforward to implement and effective to use on smaller
#   arrays. Overall, it's a decent if inefficient sorting algorithm!
# see:
# - https://en.wikipedia.org/wiki/Bubble_sort
from sys import argv


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sort(array: list) -> list:
    for _ in range(1, len(array)):
        for index in range(1, len(array)):
            if array[index - 1] >= array[index]:
                array[index - 1], array[index] = array[index], array[index - 1]
    return array


if __name__ == "__main__":
    # get user input
    if len(argv) < 2:
        exit(1)
    array = [int(argv[i]) for i in range(1, len(argv))]

    # show unsorted
    for n in array:
        print(n, end=' ')
    print("")

    # sort
    sort(array)

    # show sorted
    for n in array:
        print(n, end=' ')
    print("")
