# Jacobus Burger (2024-11-04)
# A correct implementation of insertion sort. Taken from studying
#   "Introduction to Algorithms" 3rd Edition.
#   This was practice to get better at understanding this algorithm
#   during the blackout today.


def sort(A: list[int | float]) -> list[int | float]:
    """
    Sorts an array `A` using selection sort according to the implementation
        specified in "Introduction to Algorithms 3rd Ed."

    The following pseudocode is how the algorithm should work (pg 18)

    ```
    Input: A sequence of n numbers <a1, a2, ..., an>.
    Output: A permutation (reordering) <a1', a2', ..., an'> of the input
        sequence such that a1' <= a2' <= ... <= an'.

    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into the sorted sequence A[1..j - 1]
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    ```
    """
    # Python is 0 indexed, so 2 -> 1
    # Python len gives count of elements, so maximum index is len - 1
    for j in range(1, len(A) - 1):
        key = A[j]
        i = j - 1
        pass
