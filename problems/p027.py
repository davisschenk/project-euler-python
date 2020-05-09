from problem import Problem
from utils.primes import simple_is_prime
from itertools import count


class QuadraticPrime(Problem):
    @Problem.solution()
    def brute_force(self):
        """
        Loop through all a and b values such that abs(a|b) < 1000

        then count up from 0 and check if the quadratic of the form
        n^2 + an + b until the output is not a prime and then check if we have beat
        the best n value
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
