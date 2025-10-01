/* Jacobus Burger (2025-08-02)
 * Bubble Sort (C99)
 * Bubble Sort is one of the first sorting algorithms taught in standard
 *   Computing Science courses. While it's time complexity is "bad", it's
 *   generally efficient on small volumes of data and very
 *   easy to implement.
 * see:
 * - https://en.wikipedia.org/wiki/Bubble_sort
 * - https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#C
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void sort(int *array, int length)
{
        bool unsorted = true;
        while (unsorted) {
                unsorted = false;
                for (int i = 1; i < length; i++) {
                        if (array[i - 1] > array[i]) {
                                // XOR swap
                                array[i - 1] ^= array[i];
                                array[i] ^= array[i - 1];
                                array[i - 1] ^= array[i];
                                // not sorted yet
                                unsorted = true;
                        }
                }
                length--;
        }
}

int main(void) {
        // get input
        int n;
        scanf("%i", &n);
        int *array = (int*) malloc(n * sizeof(int));
        srand(time(NULL));
        for (int i = 0; i < n; i++)
                array[i] = rand() % n;

        // show unsorted array
        for (int i = 0; i < n; i++)
                printf("%i ", array[i]);
        puts("");

        // sort array
        sort(array, n);

        // show sorted array
        for (int i = 0; i < n; i++)
                printf("%i ", array[i]);
        puts("");

        // end
        free(array);
        return 0;
}
