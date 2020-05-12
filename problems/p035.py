from problem import Problem
from utils.primes import sieve_of_eratosthenes, simple_is_prime
from itertools import permutations


class CircularPrimes(Problem):
    @Problem.solution()
    def solution(self):
        circular_primes = set()

        for prime in sieve_of_eratosthenes(1_000_000):
            if prime in circular_primes:
                continue

            if self.is_circular(prime):
                circular_primes.add(prime)

        return len(circular_primes)

    @classmethod
    def is_circular(cls, n):
        for rotation in cls.rotations(n):
            if not simple_is_prime(rotation):
                return False

        return True

    @staticmethod
    def rotations(n):
        n = str(n)

        for i in range(len(n)):
            yield int(n)
            n = n[1:] + n[:1]

