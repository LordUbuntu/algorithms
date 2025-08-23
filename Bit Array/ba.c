#include <stdio.h>
#include <limits.h>



#define BITS(A)    ( sizeof(A) * CHAR_BIT )  // bits in array block
#define ON(A, i)   ( A[i/BITS(A[0])] |= (1 << (i%BITS(A[0]))) )
#define OFF(A, i)  ( A[i/BITS(A[0])] &= (0 << (i%BITS(A[0]))) )
#define GET(A, i)  ( (A[i/BITS(A[0])] & (1 << (i%BITS(A[0])))) >> (i%BITS(A[0])) )


int main(void)
{
#define LEN 3
        int A[LEN];
        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
        puts("");

        ON(A, 6);
        ON(A, 9);
        ON(A, 69);
        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
        puts("");

        printf("6: %i\n", GET(A, 6));
        printf("7: %i\n", GET(A, 7));
        printf("69: %i\n", GET(A, 69));
        printf("70: %i\n", GET(A, 70));

        OFF(A, 6);
        OFF(A, 9);
        OFF(A, 69);
        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
}
