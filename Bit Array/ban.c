#include <stdio.h>

int main(void)
{
#define LEN 3
        int A[LEN];

        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
        puts("");

        A[0] = 64; // 6
        A[0] = 64 + 512; // 9
        A[2] = 64; // 69
        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
        puts("");

        A[0] = 0;
        A[2] = 0;
        for (size_t i = 0; i < LEN; i++) {
                printf("%032b\n", A[i]);
        }
}
