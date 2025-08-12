/* Jacobus Burger (2025-08-11)
 * Stack (C99)
 * Description:
 * Stacks are a First In Last Out (FILO) data structure where you can
 *      `push` items to the top, or `pop` items from the top, like adding
 *      and removing sheets of paper from the top of a stack of paper.
 * Complexity:
 * - Structure Space O(n)
 * - Push Time O(1) 
 * - Pop Time O(1) 
 * Info:
 * - https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct {
        int size;
        int head_index;
        int* items;
} stack;

void push(stack* s, int n);
int pop(stack* s);
