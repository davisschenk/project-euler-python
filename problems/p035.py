from problem import Problem
from utils.primes import sieve_of_eratosthenes, simple_is_prime
from itertools import permutations


class CircularPrimes(Problem):
    @Problem.solution()
    def using_lookup_table(self):
        primes = {k: False for k in sieve_of_eratosthenes(1_000_000)}

        for prime in primes.keys():
            if primes[prime]:
                continue

            if self.is_circular(prime, check_prime=lambda x: x in primes):
                primes[prime] = True

        return sum(primes.values())

    @Problem.solution()
    def using_list(self):
        circular_list = []

        for prime in sieve_of_eratosthenes(1_000_000):
            if prime in circular_list:
                continue

            if self.is_circular(prime):
                circular_list.append(prime)

        return len(circular_list)

    @Problem.solution()
    def using_set(self):
        circular_list = set()

        for prime in sieve_of_eratosthenes(1_000_000):
            if prime in circular_list:
                continue

            if self.is_circular(prime):
                circular_list.add(prime)

        return len(circular_list)

    @classmethod
    def is_circular(cls, n, check_prime=simple_is_prime):
        for rotation in cls.rotations(n):
            if not check_prime(rotation):
                return False

        return True

    @staticmethod
    def rotations(n):
        n = str(n)

        for i in range(len(n)):
            yield int(n)
            n = n[1:] + n[:1]

