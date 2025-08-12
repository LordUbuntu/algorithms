/* Jacobus Burger (2025-08-02)
 * XOR Swap (C99)
 * description:
 * A common method of swapping values is to use a temporary variable, but
 *      it is possible to swap two variables without the use of a
 *      temporary variable by utilizing a sequence of 3 xor operations.
 * see:
 * - https://en.wikipedia.org/wiki/XOR_swap_algorithm
 */
#include <stdio.h>


/* Complexity:
 * - Time: O(1)
 * - Space: O(1)
 */
void swap(void* a, void* b) {
        // XOR swap when a == b sets to 0, so avoid it
        if (a == b) return;
        // XOR swap a and b
        *a ^= *b; // a = b xor a
        *b ^= *a; // b = a xor b
        *a ^= *b; // a = b xor a
}


int main(void)
{
        int a = 1;
        int b = 2;
        printf("%i %i\n", a, b);
        swap(&a, &b);
        printf("%i %i\n", a, b);
}
