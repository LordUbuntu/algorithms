/* Jacobus Burger (2025-08-02)
 * Bubble Sort (C99)
 * see:
 * - https://en.wikipedia.org/wiki/Bubble_sort
 */
#include <stdio.h>


int* sort(int* array, int length) {
        for (int i = 1; i < length; i++)
                for (int j = 1; j < length; j++)
                        if (array[j - 1] >= array[j]) {
                                // XOR swap
                                array[j - 1] ^= array[j];
                                array[j] ^= array[j - 1];
                                array[j - 1] ^= array[j];
                        }
}


int main(void) {
        #define LEN 10

        int array[LEN] = {2, 1, 3, 7, 4, 5, 9, 8, 0, 6}

        // show unsorted array
        for (int i = 0; i < LEN; i++)
                printf("%i ", array[i]);
        puts("");

        // sort array
        sort(array, LEN);

        // show sorted array
        for (int i = 0; i < LEN; i++)
                printf("%i ", array[i]);
        puts("");

        // end
        return 0;
}
