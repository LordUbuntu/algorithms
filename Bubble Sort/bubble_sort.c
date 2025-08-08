/* Jacobus Burger (2025-08-02)
 * Bubble Sort (C99)
 * see:
 * - https://en.wikipedia.org/wiki/Bubble_sort
 */
#include <stdio.h>
#include <stdlib.h>


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


int main(int argc, char *argv[]) {
        // get user input
        if (argc < 2)
                return 1;
        int* array = (int*) malloc(sizeof(int) * argc);
        for (int i = 1; i < argc; i++)
                array[i] = atoi(argv[i]);
        
        // show unsorted
        for (int i = 1; i < argc; i++)
                printf("%i ", array[i]);
        puts("");

        // sort array
        sort(array, argc);

        // show sorted
        for (int i = 1; i < argc; i++)
                printf("%i ", array[i]);
        puts("");
}
