from math import log
from utils.primes import sieve_of_eratosthenes
from problem import Problem


class NthPrime(Problem, name="10001st prime", expected=104743):
    @Problem.solution()
    def eratosthenes_nth_prime(self, n=10001):
        # https://www.maa.org/sites/default/files/jaroma03200545640.pdf
        limit = round(n * log(n) + n * (log(log(n - 0.9385))))
        return sieve_of_eratosthenes(limit)[n - 1]
