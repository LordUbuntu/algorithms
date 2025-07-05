/* Jacobus Burger (2025-07-03)
 * Implemenation of a bit array (a linear sequence of single-bit flags)
 * See:
 * - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
 * - https://en.wikipedia.org/wiki/Bit_array
 */
// note for implementation: sizeof can be used to calculate bytes of int
//      type at runtime, and thus can be used to calculate bits per
//      address in array. Then the emory info can be used to produce
//      macros for setting and reading bits along an array
//      This can be used in the sieve_of_eratosthenes.c file!
#include <limits.h>
#include <stdio.h>
#include <stddef.h>


#define BITS(DATA)   ( sizeof(DATA) * CHAR_BIT )
#define SET(A, i)    ( A[(i / BITS(A[0]))] |= (1 << (i % BITS(A[0]))) )
#define GET(A, i)    ( A[(i / BITS(A[0]))] & (1 << (i % BITS(A[0]))) )
#define TOGGLE(A, i) ( A[(i / BITS(A[0]))] ^= (1 << (i % BITS(A[0]))) )
#define CLEAR(A, i)  ( A[(i / BITS(A[0]))] &= ~(1 << (i % BITS(A[0]))) )


int main(int argc, char *argv[]) {
        int A[3];

        // show initial state
        printf("INITIAL STATE\n");
        printf("bits in int: %i\n", BITS(A[0]));
        for (size_t i = 0; i < 3; i++)
                printf("A[%i] = %032b\n", i, A[i]);
        printf("\n");

        // set bits
        SET(A, 30);
        SET(A, 50);
        SET(A, 70);

        // show change in state
        for (size_t i = 0; i < 3; i++)
                printf("A[%i] = %032b\n", i, A[i]);
        printf("\n");

        // test get
        for (size_t i = 0; i < 3 * BITS(A[0]); i++)
                if (GET(A, i))
                        printf("bit %i is set\n", i);

        // toggle bit
        printf("state before toggle: %032b\n", A[0]);
        TOGGLE(A, 7);
        printf("state after toggle: %032b\n", A[0]);

        // test clear
        printf("state before clear: %032b\n", A[0]);
        CLEAR(A, 30);
        if (~GET(A, 30))
                printf("unset successful\n");
        printf("state before clear: %032b\n", A[0]);
}
