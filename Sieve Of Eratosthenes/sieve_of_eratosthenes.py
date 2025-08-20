# Jacobus Burger (2022)
# Sieve of Eratosthenes (Python 3)
# The Sieve of Eratosthenes is an ancient and effective algorithm for finding
#      all the prime numbers up to a given limit through a process of
#      elimination (like how a sieve filters out bigger particles). It does
#      this by iteratively canceling out all the multiples of numbers starting
#      from the first known prime number 2, thus canceling out every even
#      number besides 2, then it starts with the next number which is then
#      known to be prime too, and it keeps iterating on this process until all
#      composite numbers are eliminated. Once all known composites are
#      removed, what remains are all the prime numbers in the range!
# Info:
# - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
from sys import argv
from math import sqrt as sqrt


# Time Complexity: O(n log log n)
# Space Complexity: O(n)
def sieve(n: int):
    # initialize all except 0 and 1 to True
    primes = [True if i > 1 else False for i in range(n + 1)] # iterate through all integers from 2 to sqrt(n)
    for p in range(2, int(sqrt(n)) + 1):
        # skip any non-primes
        if primes[p] == True:
            # eliminate all multiples i of current prime p, from p^2 to n
            for i in range(p**2, n + 1, p):
                primes[i] = False
    # you now have the sieve of eratosthenes
    return primes


if __name__ == "__main__":
    # get n
    n = int(argv[1])
    # get list of prime numbers using sieve and list comprehension
    primes = " ".join([str(i) for i in range(len(sieve(n))) if prime_sieve[i]])
    # print result
    print("{}\n{}\n\n".format(n, primes))
