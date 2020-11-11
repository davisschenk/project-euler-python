from itertools import count

from problem import Problem
from utils.primes import simple_is_prime


class QuadraticPrime(Problem, name="Quadratic primes", expected=-59231):
    @Problem.solution()
    def brute_force(self):
        """
        Loop through all a and b values such that abs(a|b) < 1000

        then count up from 0 (n) and check if the output of the quadratic
        n^2 + an + b for each n until the output is no longer a prime
        check if we beat the max and then rinse and repeat
        """
        best_a, best_b, best_n = 0, 0, 0

        for a in range(-1000, 1000):
            for b in range(-1000, 1000):
                for n in count():
                    output = (n ** 2) + (a * n) + b

                    if not simple_is_prime(output):
                        if best_n < n - 1:
                            best_a = a
                            best_b = b
                            best_n = n - 1

                        break
        return best_a * best_b
