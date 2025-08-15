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
                int ret = realloc(array->data, sizeof(n) * array->capacity);
                if (!ret)
                        exit(1);
        }
        array->data[array->size] = n;
        array->size++;
}
