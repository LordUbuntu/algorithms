# Jacobus Burger (2023-06-02)
# Binary Search (Python 3)
# Descrption:
# Binary Search, find an element in a sorted array by dividing the
#      search area in half to the left or right each time until the
#      desired value is found (or not).
# Complexity:
# - time: O(log n)
# - space: O(1)
# Info:
# - https://en.wikipedia.org/wiki/Binary_search_algorithm


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


if __name__ == "__main__":
    # create array
    array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31]
    # show array
    for n in array:
        print(n, end=' ')
    print("")
    # show location
    print("13 located at {}".format(search(array, 13)))
