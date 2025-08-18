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

typedef struct {
        size_t capacity;
        size_t size;
        int *data;
} dynarr_t;

/* Time Complexity: O(1)
 * Space Complexity: O(n), on realloc O(2n)
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

dynarr_t* new_dynarr(void)
{
        dynarr_t* array = (dynarr_t*) malloc(sizeof(dynarr_t));
        array->size = 0;
        array->capacity = 1;
        array->data = (int*) malloc(sizeof(int));
        return array;
}

void free_dynarr(dynarr_t* array)
{
        free(array->data);
        free(array);
        array = NULL;
}

int main(void)
{
        dynarr_t* array = new_dynarr();
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
        free_dynarr(array);
}
