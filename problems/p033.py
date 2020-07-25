from itertools import count

from problem import Problem
from utils.math import get_first_digit, gcd


class DigitCancellingFraction(Problem):
    @Problem.solution()
    def brute_force(self):
        non_trivial = set()

        # This loop goes from 10/10 up and check if the fraction is cancelling
        for d in count(start=10):
            for n in range(10, d):

                if self.is_cancelling_fraction(n, d):
                    non_trivial.add((n, d))

                    if len(non_trivial) == 4:
                        # Return denominator of simplified product of fractions
                        numerator, denominator = self.fraction_product(non_trivial)

                        return denominator

    @classmethod
    def fraction_product(cls, fractions):
        total_n = 1
        total_d = 1

        for n, d in fractions:
            total_n *= n
            total_d *= d

        return cls.simplify(total_n, total_d)

    @classmethod
    def is_cancelling_fraction(cls, n, d):
        last_numerator_digit = n % 10
        rest_n = int(n / 10)

        first_denominator_digit = get_first_digit(d)
        rest_d = d % 10

        if last_numerator_digit == first_denominator_digit and rest_d != 0 and rest_n != 0:
            simplified = cls.simplify(n, d)
            bad_simplified = (rest_n, rest_d)

            return simplified[0] / simplified[1] == bad_simplified[0] / bad_simplified[1]

        return False

    @staticmethod
    def simplify(n, d):
        s = gcd(n, d)

        return n / s, d / s
