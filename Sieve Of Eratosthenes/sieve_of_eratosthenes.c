/* Jacobus Burger (2025)
 * Sieve of Eratosthenes in C
 * see: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 *
 * note: when compiling be sure to link math library. eg: -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


bool *sieve(int n) {
        // initialize array to all true except for index/numbers 0 and 1
        bool *primes = (bool*) calloc(n, sizeof(bool));
        memset(primes + 2, 1, n * sizeof(bool));

        // run sieve of eratosthenes
        for (int p = 2; p < sqrt(n) + 1; p++)
                // ignore non-primes
                if (primes[p])
                        // eliminate multiples of p starting from p^2
                        for (int i = pow(p, 2); i < n + 1; i += p)
                                primes[i] = 0;

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
                if (primes[i])
                        printf("%i ", i);
                else
                        continue;
        }
        printf("\n\n");
        // end program
        free(primes);
        return 0;
}
