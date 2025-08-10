# Jacobus Burger (2022)
# Bubble Sort (Python 3)
# see:
# - https://en.wikipedia.org/wiki/Bubble_sort
from sys import argv


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
