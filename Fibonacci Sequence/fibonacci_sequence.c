/* Jacobus Burger (2025-08-29)
 * Fibonacci Sequence (C99)
 * Description:
 * Fibonacci Sequence is a recursive mathematical sequence where every
 *   subsequent value Fn = Fn-1 + Fn-2. It often starts like
 *   1 1 2 3 5 8 13 ...
 * Info:
 * - https://en.wikipedia.org/wiki/Fibonacci_sequence
 * - https://rosettacode.org/wiki/Fibonacci_sequence#C
 */
#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n)
{
        if (n <= 1) {
                return 1;
        }

        int a = 1, b = 1, temp = 0;
        for (size_t i = 0; i < n - 1; i++) {
                temp = b;
                b = a + b;
                a = temp;
        }
        return b;
}

int main(int argc, char *argv[])
{
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);
        printf("fib n = %i\n", fibonacci(n));
}
