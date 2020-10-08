from itertools import count

from problem import Problem
from utils.primes import sieve_of_eratosthenes


class ReciprocalCycles(Problem):
    @Problem.solution()
    def solution(self):
        # Best number, best cycle length
        best_n, best_c = 0, 0

        # Only really need to check primes
        for i in sieve_of_eratosthenes(1000):
            # Infinite loop if i is divisible by 2 or 5
            if i % 2 != 0 and i % 5 != 0:
                cn = self.cycle_length(i)

                # Keep track of max
                if best_c < cn:
                    best_n = i
                    best_c = cn

        return best_n

    @classmethod
    def cycle_length(cls, b):
        c = 1

        for i in count():
            c = c * 10 % b

            if c == 1:
                return i + 1

    # I need to come back and fix this
    # @classmethod
    # def find_period(cls, denominator):
    #     # This works but has overflow issues :(
    #     # https://math.stackexchange.com/questions/377683/length-of-period-of-decimal-expansion-of-a-fraction
    #     max_period = 1
    #     for i in factors(cls.eulers_totient(denominator)):
    #         repeating = int((10 ** i) * (1/denominator))
    #         if 1 / denominator == repeating / ((10**i) - 1):
    #             max_period = max(max_period, i)
    #
    #     return max_period
    #
    # @staticmethod
    # def eulers_totient(n):
    #     result = 1
    #
    #     for i in range(2, n):
    #         if gcd(i, n) == 1:
    #             result += 1
    #
    #     return result
