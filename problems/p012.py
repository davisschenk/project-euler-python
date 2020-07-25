from itertools import count

from problem import Problem
from utils.math import factors
from utils.primes import sieve_of_eratosthenes


class HighlyDivisibleTriangleNumber(Problem, name="Highly divisible triangular number", expected=76576500):
    @Problem.solution()
    def brute_force(self):
        for i in count(3):
            triangle_number = sum(range(1, i))

            if len(factors(triangle_number)) > 500:
                return triangle_number

    # @Problem.solution()
    def prime(self):
        primes = sieve_of_eratosthenes(1000)
        n = 3
        prime_divisors = 2
        c = 0

        while c <= 500:
            print(c)
            n += 1
            n1 = n

            if n1 % 2 == 0:
                n1 /= 2
            dn1 = 1

            for prime in primes:
                if prime * prime > n1:
                    dn1 *= 2
                    break

                exponent = 1

                while n1 % prime == 0:
                    exponent += 1
                    n1 /= prime

                if exponent > 1:
                    dn1 *= exponent

                if n1 == 1:
                    break

            c = prime_divisors * dn1
            prime_divisors = dn1

        return n * (n - 1) / 2
