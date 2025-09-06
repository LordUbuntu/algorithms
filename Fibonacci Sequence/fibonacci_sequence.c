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

long long fibonacci(int n)
{
        // inspired by Uiua's automatic inversion, i just need to swap
        //      around a and b for the negative recurrence of
        //      Fibonacci sequence
        long long a = 0, b = 1, temp = a;
        // n >= 0
        for (int i = 0; i < n; i++) {
                temp = b;
                b = a + b;
                a = temp;
        }
        // n < 0
        for (int i = n; i < 0; i++) {
                temp = a;
                a = b - a;
                b = temp;
        }
        return a;
}

int main(void)
{
        int n;
        scanf("%i", &n);
        printf("fib %i = %lli\n", n, fibonacci(n));
}
