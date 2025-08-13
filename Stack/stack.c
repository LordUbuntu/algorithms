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

#define LEN 10

/* Stack Abstract Data Type (ADT)
 * size_t head: top of stack index (and size of stack)
 * unsigned data[LEN]: array of data (static data for now)
 */
typedef struct {
        size_t head;
        unsigned data[LEN];
} stack;

void push(stack *s, int value)
{
        if (s->head + 1 >= LEN)
                return;
        s->data[s->head] = value;
        s->head++;
}

int pop(stack *s)
{
        if (s->head <= 0)
                return -1;
        s->head--;
        int value = s->data[s->head];
        return value;
}

int main(void)
{
        stack s;
        printf("%i %i\n", s.head, sizeof(s));
        push(&s, 1);
        push(&s, 2);
        push(&s, 3);
        printf("%i %i\n", s.head, sizeof(s));
        printf("%i\n", pop(&s));
        printf("%i\n", pop(&s));
        printf("%i\n", pop(&s));
        printf("%i\n", pop(&s));
        printf("%i %i\n", s.head, sizeof(s));
}
