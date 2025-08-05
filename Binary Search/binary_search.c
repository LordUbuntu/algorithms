// Jacobus Burger (2023-06-02)
// Binary Search (C99)
// Descrption:
// Binary Search, find an element in a sorted array by dividing the
//      search area in half to the left or right each time until the
//      desired value is found (or not).
// Complexity:
// - time: O(log n)
// - space: O(1)
// Info:
// - https://en.wikipedia.org/wiki/Binary_search_algorithm
#include <stdio.h>


int search(int* array, int length, int target) {
        int left = 0, right = length - 1;
        while (left <= right) {
                int middle = (left + right) / 2;
                if (target == array[middle]) {
                        return middle;
                } else if (target > array[middle]) {
                        left = middle + 1;
                } else if (target < array[middle]) {
                        right = middle - 1;
                }
        }
        return -1;
}


int main(void) {
        int arr[5] = {1, 3, 4, 7, 8};
        printf("target: %i, result: %i\n", 3, search(arr, 5, 3));
}
