# Jacobus Burger (2022)
# Sieve of Eratosthenes in Python
# see: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
from sys import argv
from math import sqrt as sqrt


def sieve(n: int):
    # initialize all except 0 and 1 to True
    sieve = [True if i > 1 else False for i in range(n + 1)]
    # iterate through all integers from 2 to sqrt(n)
    for p in range(2, int(sqrt(n)) + 1):
        # skip any non-primes
        if sieve[p] == True:
            # eliminate all multiples i of current prime p, from p^2 to n
            for i in range(p**2, n + 1, p):
                sieve[i] = False
    # you now have the sieve of eratosthenes
    return sieve


if __name__ == "__main__":
    # get n
    n = int(argv[1])
    # sieve primes up to n
    prime_sieve = sieve(n)
    # get list of prime numbers using sieve and list comprehension
    primes = " ".join([str(i) for i in range(len(prime_sieve)) if prime_sieve[i]])
    # print result
    print("{}\n{}\n\n".format(n, primes))
