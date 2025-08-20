/* Jacobus Burger (2025)
 * Sieve of Eratosthenes (C99)
 * The Sieve of Eratosthenes is an ancient and effective algorithm for finding
 *      all the prime numbers up to a given limit through a process of
 *      elimination (like how a sieve filters out bigger particles). It does
 *      this by iteratively canceling out all the multiples of numbers starting
 *      from the first known prime number 2, thus canceling out every even
 *      number besides 2, then it starts with the next number which is then
 *      known to be prime too, and it keeps iterating on this process until all
 *      composite numbers are eliminated. Once all known composites are
 *      removed, what remains are all the prime numbers in the range!
 * Info:
 * - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 * Compilation:
 * - gcc sieve_of_eratosthenes.c -lm -o sieve
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


/* Time Complexity: O(n log log n)
 * Space Complexity: O(n)
 */
bool *sieve(int n) {
        // initialize array to all true except for index/numbers 0 and 1
        bool *primes = (bool*) calloc(n, sizeof(bool));
        memset(primes + 2, 1, n * sizeof(bool));

        // run sieve of eratosthenes
        for (int p = 2; p < sqrt(n) + 1; p++) {
                // ignore non-primes
                if (primes[p]) {
                        // eliminate multiples of p starting from p^2
                        for (int i = pow(p, 2); i < n + 1; i += p) {
                                primes[i] = 0;
                        }
                }
        }

        // return solution
        return primes;
}


int main(int argc, char *argv[]) {
        // get n
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);
        // get sieve
        bool *primes = sieve(n);
        // print result
        printf("%i\n", n);
        for (int i = 0; i < n; i++) {
                // print array elements that are prime
                if (primes[i]) {
                        printf("%i ", i);
                }
        }
        printf("\n\n");
        // end program
        free(primes);
        return 0;
}
