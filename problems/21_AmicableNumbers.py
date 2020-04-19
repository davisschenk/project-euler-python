from problem import Problem
from utils.math import factors
import math


class AmicableNumbers(Problem, name="Amicable numbers", expected=31626):
    @classmethod
    def sum_of_divisors(cls, n):
        """
        This is a fancy way of finding the sum of divisors but it actually slower then just finding all factors and then
        summing
        """
        res = 1
        for i in range(2, int(math.sqrt(n) + 1)):
            curr_sum = 1
            curr_term = 1

            while n % i == 0:
                n /= i

                curr_term *= i
                curr_sum += curr_term

            res *= curr_sum

        if n > 2:
            res *= (1 + n)

        return res

    @classmethod
    def sum_of_proper_divisors(cls, n):
        return cls.sum_of_divisors(n) - n

    @Problem.solution(ignored=True)
    def finding_pairs_in_dict(self, max_n=10000):
        """
        We find all factor sums and then manually find pairs. This is really inefficient
        """
        div_sums = {n: sum(factors(n)) - n for n in range(1, max_n)}

        return sum(
            item[0] for item in div_sums.items() for check in div_sums.items() if
            item == check[::-1] and item[0] != item[1])

    @Problem.solution()
    def smarter_pairs(self, max_n=10000):
        s = 0

        for a in range(2, max_n):
            b = self.sum_of_proper_divisors(a)

            if b > a and self.sum_of_proper_divisors(b) == a:
                s += a + b

        return s
