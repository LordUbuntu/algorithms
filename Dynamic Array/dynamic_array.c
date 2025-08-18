/* Jacobus Burger (2025-08-14)
 * Dynamic Array Data Structure (C99):
 * Dynamic / Growable Arrays are random access list Data Structures that
 *      can have be dynamically resized at runtime. They're not available
 *      natively in some languages (such as C) but can be implemented.
 * Info:
 * - https://en.wikipedia.org/wiki/Dynamic_array
 */
#include <stdlib.h>
#include <stdio.h>

/* Dynamic / Growable Array Abstract Data Type (ADT)
 * size_t capacity: allocated space for array
 * size_t size: currently used space for array
 * int *data: underlying dynamically allocated memory region for array
 */
typedef struct {
        size_t capacity;
        size_t size;
        int *data;
} dynarr_t;

/* Time Complexity: O(1), O(n) for realloc
 * Growth Factor: 2
 */
void insert(dynarr_t *array, int n)
{
        // realloc space when capacity reached
        if (array->size >= array->capacity) {
                array->capacity = array->capacity * 2;
                array->data = (int*) realloc(array->data, sizeof(n) * array->capacity);
                if (!array->data)
                        exit(1);  // failure to realloc memory
        }
        array->data[array->size] = n;
        array->size++;
}

int main(void)
{
        // allocate array for demo
        dynarr_t* array = (dynarr_t*) malloc(sizeof(dynarr_t));
        array->size = 0;
        array->capacity = 1;
        array->data = (int*) malloc(sizeof(int));

        // show off array functions
        printf("size: %i, capacity: %i, first: %i\n", array->size, array->capacity, array->data[0]);
        insert(array, 1);
        insert(array, 2);
        insert(array, 3);
        insert(array, 4);
        insert(array, 5);
        printf("size: %i, capacity: %i, first: %i\n", array->size, array->capacity, array->data[0]);
        printf("data: ");
        for (int i = 0; i < array->size; i++)
                printf("%i ", array->data[i]);
        puts("");

        // free dynamically allocated dynamic array
        free(array->data);
        free(array);
        array = NULL;
}
