# Jacobus Burger (2023)
# binary search on an array of values, O(log n) time
# see: https://en.wikipedia.org/wiki/Binary_search_algorithm
def search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target >= array[mid]:
            low = mid + 1
        elif target < array[mid]:
            high = mid - 1
    return -1


if __name__ == '__main__':
    array = [1, 3, 4, 7, 8]
    print("target: ", 3, "result: ", search(array, 3))
    print("target: ", 10, "result: ", search(array, 10))
