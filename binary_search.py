# Jacobus Burger (2023)
# binary search on an array of values, O(log n) time
# see: https://en.wikipedia.org/wiki/Binary_search_algorithm
def search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target >= nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1
