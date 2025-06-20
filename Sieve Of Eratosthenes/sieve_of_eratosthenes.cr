# Jacobus Burger (2025-06-20)
# Sieve of Eratosthenes in Crystal
# see: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def sieve(n : Int64)
  primes : Array(Bool) = Array.new(n + 1) { |i| i < 2 ? false : true }

  (2 .. Math.sqrt(n) + 1).each do |p|
    if primes[p]
      (p**2 .. n).step(p) do |i|
        primes[i] = false
      end
    end
  end
  return primes
end


def main
  n = gets.try(&.to_i) || 0
  puts "#{sieve(n)}"
end


main
