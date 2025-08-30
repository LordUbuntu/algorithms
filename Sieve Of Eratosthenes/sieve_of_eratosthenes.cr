# Jacobus Burger (2025-06-20)
# Sieve of Eratosthenes (Crystal 1.17)
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


# Time Complexity: O(n log log n)
# Space Complexity: O(n)
def sieve(n : Int64)
  primes : Array(Bool) = Array.new(n + 1) { |i| i < 2 ? false : true }

  (2 .. Math.sqrt(n) + 1).each do |p|
    if primes[p]
      (p**2 .. n).step(p) do |i|
        primes[i] = false
      end
    end
  end
  primes
end


def main
  # get n
  n = gets.try(&.to_i) || 0
  # get list of primes
  primes = sieve(n)
  # print result
  puts n
  n.times do |i|
    if primes[i]
      print "#{i} "
    end
  end
  puts
  puts
end


main
