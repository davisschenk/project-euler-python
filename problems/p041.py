from problem import Problem
from itertools import permutations
from utils.primes import sieve_of_eratosthenes, simple_is_prime
from problems.p032 import PandigitalProducts


class PandigitalPrime(Problem):
    @Problem.solution()
    def solution(self):
        for i in (7, 4):  # all other lengths of n are divisible by 3
            digits = reversed("123456789"[:i])
            for j in permutations(digits):
                j = int(''.join(j))
                if simple_is_prime(j):
                    return j


