from math import log

from more_itertools import nth

from problem import Problem
from utils.primes import sieve_of_eratosthenes


class NthPrime(Problem, name="10001st prime", expected=104743):
    @Problem.solution()
    def eratosthenes_nth_prime(self, n=10001):
        # This is a mathmatical function which can approximately predict the limit for the nth prime
        # https://www.maa.org/sites/default/files/jaroma03200545640.pdf
        limit = round(n * log(n) + n * (log(log(n - 0.9385))))
        return nth(sieve_of_eratosthenes(limit), n - 1)
