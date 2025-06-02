// Jacobus Burger (2023)
// binary search on an array of values, O(log n) time
// see: https://en.wikipedia.org/wiki/Binary_search_algorithm
#include <stdio.h>


// TODO: live life dangerously and generically with void*
int search(int target, int *array, int length) {
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
        printf("target: %i, result: %i\n", 3, search(3, arr, 5));
        printf("target: %i, result: %i\n", 10, search(10, arr, 5));
}
