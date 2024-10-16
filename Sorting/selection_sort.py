# Jacobus Burger (2023)
# A simple selection sort algorithm

def sort(array: list) -> list:
    for current in range(len(array)):
        minimum = current  # assume minimum is first element
        # search for a smaller value after current
        for index in range(current + 1, len(array)):
            if array[index] < array[minimum]:
                minimum = index
        # swap elements
        array[current], array[minimum] = array[minimum], array[current]
    return array
