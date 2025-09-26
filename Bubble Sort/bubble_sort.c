/* Jacobus Burger (2025-08-02)
 * Bubble Sort (C99)
 * Bubble Sort is one of the first sorting algorithms taught in standard
 *   Computing Science courses. While it's time complexity is "bad", it's
 *   generally efficient on small volumes of data and very
 *   easy to implement.
 * see:
 * - https://en.wikipedia.org/wiki/Bubble_sort
 */
#include <stdio.h>

/* Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */
void sort(int *array, int length)
{
        for (int i = 1; i < length; i++) {
                for (int j = 1; j < length; j++) {
                        if (array[j - 1] >= array[j]) {
                                // XOR swap
                                array[j - 1] ^= array[j];
                                array[j] ^= array[j - 1];
                                array[j - 1] ^= array[j];
                        }
                }
        }
}

int main(void) {
        #define LEN 10

        int array[LEN] = {2, 1, 3, 7, 4, 5, 9, 8, 0, 6}

        // show unsorted array
        for (int i = 0; i < LEN; i++) {
                printf("%i ", array[i]);
        }
        puts("");

        // sort array
        sort(array, LEN);

        // show sorted array
        for (int i = 0; i < LEN; i++) {
                printf("%i ", array[i]);
        }
        puts("");

        // end
        return 0;
}
