/* Jacobus Burger (2025-08-29)
 * Fibonacci Sequence (C99)
 * Fibonacci Sequence is a recursive mathematical sequence where every
 *   subsequent value Fn = Fn-1 + Fn-2. It often starts like F0 = F1 = 1,
 *   interestingly it works bi-directionally in both positive and
 *   negative values for n.
 *                               F0 F1
 *   13, -8, 5, -3, 2, -1, 1, 0, 1  1  2 3 5 8 13 ...
 * Info:
 * - https://en.wikipedia.org/wiki/Fibonacci_sequence
 * - https://rosettacode.org/wiki/Fibonacci_sequence#C
 */
#include <stdio.h>

int fibonacci(int n)
{
        // TODO: make work for all int
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

int main(void)
{
        int n;
        scanf("%i", &n);
        printf("fib %i = %i\n", n, fibonacci(n));
}
