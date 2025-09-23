/* Jacobus Burger (2025-09-04)
 * Triangle Numbers (C99)
 * Description:
 * Triangle Numbers are a count of the number of objects arranged in
 *   an equilateral traingle for a given row number.
 *     .    1 = 1
 *    . .   2 = 3
 *   . . .  3 = 6
 *  . . . . 4 = 10
 *  etc...
 * Info:
 * - https://en.wikipedia.org/wiki/Triangular_number
 */
#include <stdio.h>
#include <stdlib.h>

unsigned triangle_numbers(unsigned n)
{
        unsigned sum = 0;
        for (size_t i = 1; i <= n; i++)
                sum += i;
        return sum;
}

int main(void)
{
        unsigned n;
        scanf("%u", &n);
        printf("%u\n", triangle_numbers(n));
}
