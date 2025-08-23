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
void insert_data(dynarr_t *array, int n)
{
        // realloc space when capacity reached
        if (array->size >= array->capacity) {
                array->capacity = array->capacity * 2;
                array->data = (int*) realloc(array->data, sizeof(int) * array->capacity);
                if (!array->data)
                        exit(1);  // failure to realloc memory
        }
        array->data[array->size] = n;
        array->size++;
}

/* Time Complexity: O(1), O(n) for realloc
 * Shrink Factor: 2
 */
int remove_data(dynarr_t *array)
{
        // get element from array
        if (array->size <= 0)
                return -1;
        array->size--;
        int value = array->data[array->size];
        // realloc space when capacity reduced
        if (array->size < array->capacity / 2 && array->size > 1) {
                array->capacity = array->capacity / 2;
                array->data = (int*) realloc(array->data, sizeof(int) * array->capacity);
                if (!array->data)
                        exit(1);  // failure to realloc memory
        }
        return value;
}

int main(void)
{
        // allocate array for demo
        dynarr_t *array = (dynarr_t*) malloc(sizeof(dynarr_t));
        array->size = 0;
        array->capacity = 1;
        array->data = (int*) malloc(sizeof(int));

        // grow array by 5
        printf("size: %zu, capacity: %zu, first: %i\n", array->size, array->capacity, array->data[0]);
        for (int i = 1; i < 6; i++) {
                insert_data(array, i);
        }
        printf("size: %zu, capacity: %zu, first: %i\n", array->size, array->capacity, array->data[0]);
        printf("data: ");
        for (int i = 0; i < array->size; i++) {
                printf("%i ", array->data[i]);
        }
        puts("");

        // shrink array by 5
        printf("size: %zu, capacity: %zu, first: %i\n", array->size, array->capacity, array->data[0]);
        for (int i = 0; i < 5; i++) {
                printf(" %i\n", remove_data(array));
        }
        printf("size: %zu, capacity: %zu, first: %i\n", array->size, array->capacity, array->data[0]);
        printf("data: ");
        for (int i = 0; i < array->size; i++) {
                printf("%i ", array->data[i]);
        }
        puts("");

        // free dynamically allocated dynamic array
        free(array->data);
        free(array);
        array = NULL;
}
