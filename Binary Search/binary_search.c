// Jacobus Burger (2023)
// binary search on an array of values, O(log n) time
// see: https://en.wikipedia.org/wiki/Binary_search_algorithm
#include <stdio.h>
#include <stddef.h>


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


// living dangerously with a generic version
int binary_search(
        void *array,
        size_t length,
        size_t element_size,
        void *target,
        int (*cmp)(void* a, void* b)
) {
        size_t left = 0;
        size_t right = length - 1;
        while (left <= right) {
                size_t middle = (left + right) / 2;
                void *current = array + (element_size * middle);
                int diff = cmp(target, current);
                if (diff == 0) {
                        return middle;
                } else if (diff > 0) {
                        left = middle + 1;
                } else if (diff < 0) {
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
