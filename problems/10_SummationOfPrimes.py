from utils.primes import sieve_of_eratosthenes, simple_is_prime
from problem import Problem


class SummationOfPrimes(Problem, name="Summation of primes", expected=142913828922):
    @Problem.solution()
    def sieve_of_eratosthenes(self, n=2_000_000):
        return sum(filter(lambda x: x <= n, sieve_of_eratosthenes(n)))

    @Problem.solution()
    def brute_force(self, limit=2_000_000):
        return 5 + sum(filter(simple_is_prime, range(5, limit + 1, 2)))

