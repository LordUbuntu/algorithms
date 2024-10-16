# Jacobus Burger (2022)
# Bubble Sort
# Bubble sort compaires pairs of adjacent values and swaps them
#     if they're out of order. It's worst case is O(n^2). So not
#     great on big inputs...
def sort(array: list) -> list:
    for _ in range(1, len(array)):
        sorted = True
        for index in range(1, len(array)):
            if array[index - 1] >= array[index]:
                sorted = False
                array[index - 1], array[index] = array[index], array[index - 1]
        if sorted:
            break
    return array
