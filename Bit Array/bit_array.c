/* Jacobus Burger (2025-07-03)
 * Bit Array (C99)
 * Description:
 * Bit Array, a block of data like an array of integers is treated as a
 *      large contiguous array of single bit flags, useful for
 *      representing a large array of booleans in a space efficient way.
 * See:
 * - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
 * - https://en.wikipedia.org/wiki/Bit_array
 */
#include <limits.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>


/* the underlying principle is simple, we select the i / bits block of
 *      bits, which is each index of the array A, then we select the
 *      i % bits bit from that block. Thus we treat an array A as a
 *      continguous segment of memory of single bits equal in count
 *      to bits * length of A.
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */
#define BITS(DATA)   ( sizeof(DATA) * CHAR_BIT )
#define SET(A, i)    ( A[(i / BITS(A[0]))] |= (1 << (i % BITS(A[0]))) )
#define GET(A, i)    ( A[(i / BITS(A[0]))] & (1 << (i % BITS(A[0]))) )
#define TOGGLE(A, i) ( A[(i / BITS(A[0]))] ^= (1 << (i % BITS(A[0]))) )
#define CLEAR(A, i)  ( A[(i / BITS(A[0]))] &= ~(1 << (i % BITS(A[0]))) )


int main(int argc, char *argv[]) {
        // get input
        if (argc < 2)
                return 1;
        size_t n = atoi(argv[1]);

        // setup initial state
        uint64_t A[4];
        printf("memory:\n");
        printf("%064b\n%064b\n%064b\n%064b\n", A[0], A[1], A[2], A[3]);
        printf("%i bits in total\n\n", BITS(A[0]) * 4);

        // set bits
        SET(A, n);
        printf("set bit %i\n", n);
        printf("memory:\n");
        printf("%064b\n%064b\n%064b\n%064b\n", A[0], A[1], A[2], A[3]);

        printf("bit %i is set: %s\n", n, GET(A, n) ? "T" : "F");

        // toggle bit
        TOGGLE(A, n);
        printf("toggled bit %i: %s\n", n, GET(A, n) ? "T" : "F");
        TOGGLE(A, n);
        printf("toggled bit %i: %s\n", n, GET(A, n) ? "T" : "F");

        // test clear
        CLEAR(A, n);
        printf("cleared bit %i: %s\n", n, GET(A, n) ? "T" : "F");

        // show final state
        printf("memory:\n");
        printf("%064b\n%064b\n%064b\n%064b\n", A[0], A[1], A[2], A[3]);
}
