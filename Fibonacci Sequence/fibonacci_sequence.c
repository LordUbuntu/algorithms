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
        // F0 = 0, F1 = 1
        // Fn = Fn+2 - Fn+1
        // F2 = F4 - F3 = 3 - 2 = 1
        // F1 = F3 - F2 = 2 - 1 = 1
        // F0 = F2 - F1 = 1 - 1 = 0
        // F-1 = F1 - F0 = 1 - 0 = -1
        // F-2 = F0 - F-1 = 0 - -1 = 1
        // This works, but how to calculate future terms ahead?
        // Uiua one works symetrically because for negative n it
        //      inverts the functions, so `off add` becomes
        //      `with backward sub`, which means that it should be
        //      posssible to get a similar logic going in C and
        //      other more imperative languages.
        long long a = 0, b = 1, temp = 1;
        while (n-- > 0) {
                temp = a + b;
                a = b;
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
