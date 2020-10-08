from itertools import count

from problem import Problem
from utils.math import prime_factors


class DistinctPrimeFactors(Problem):
    @Problem.solution()
    def brute_force(self):
        for start in count(2):
            curr = start
            consecutive = []

            while len(set(prime_factors(curr))) == 4:
                consecutive.append(curr)
                curr += 1

            if len(consecutive) == 4:
                return consecutive[0]

    @Problem.solution()
    def sieve(self):
        max_v = 1_000_000
        sieve = [0] * max_v

        for i in range(2, int(max_v ** 0.5)):
            if sieve[i] != 0:
                continue

            for a in range(2 * i, max_v, i):
                sieve[a] += 1

        consecutive = 0
        for i in range(644, max_v):
            if sieve[i] < 4:
                consecutive = 0
                continue

            consecutive += 1

            if consecutive == 4:
                return i - 3

