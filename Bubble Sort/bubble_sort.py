# Jacobus Burger (2022)
# Bubble Sort (Python 3)
# see:
# - https://en.wikipedia.org/wiki/Bubble_sort


def sort(array: list) -> list:
    for _ in range(1, len(array)):
        for index in range(1, len(array)):
            if array[index - 1] >= array[index]:
                array[index - 1], array[index] = array[index], array[index - 1]
    return array
