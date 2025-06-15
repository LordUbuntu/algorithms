/* Jacobus Burger (2025)
 * Sieve of Eratosthenes in C
 * see: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool *sieve(int n) {
        // initialize array to all true except for index 0 (the number 1)
        bool *primes = (bool*) calloc(n, sizeof(bool));
        memset(primes + 1, 1, n * sizeof(bool));

        // run sieve of eratosthenes
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
                printf("%i ", primes[i]);
                // // print array elements that are prime
                // if (primes[i])
                //         printf("%i ", i + 1);
                // else
                //         continue;
        }
        printf("\n\n");
        // end program
        free(primes);
        return 0;
}
