from itertools import takewhile, count

from problem import Problem
from utils.primes import sieve_of_eratosthenes, simple_is_prime


class GoldbachsOtherConjecture(Problem, name="Goldbach's other conjecture", expected=5777):
    @Problem.solution()
    def brute_force(self):
        primes = list(sieve_of_eratosthenes(10000))
        composites = set(range(3, 10000)) - set(primes)

        for composite in filter(lambda c: c % 2, composites):
            success = False

            for prime in takewhile(lambda p: p < composite, primes):
                for square in range(1, int(composite ** 0.5)):
                    out = prime + (2 * (square ** 2))

                    if composite == out:
                        success = True
                        break

                if success:
                    break

            if not success:
                return composite

    @Problem.solution()
    def improved_brute_force(self):
        primes = list(sieve_of_eratosthenes(10000))
        composites = set(range(3, 10000)) - set(primes)

        for composite in filter(lambda c: c % 2, composites):
            square = 0

            while 2 * (square ** 2) <= composite:
                out = composite - 2 * square ** 2

                if out in primes:
                    break

                square += 1
            else:
                return composite

    @Problem.solution()
    def sieve_less(self):
        for composite in count(35, 2):
            # ignore odd primes
            if simple_is_prime(composite):
                continue

            for i in count():
                delta = composite - 2 * i ** 2

                if delta < 2:
                    return composite

                if simple_is_prime(delta):
                    break
