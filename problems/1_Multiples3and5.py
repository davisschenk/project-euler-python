from itertools import count, takewhile
from problem import Problem


class MultiplesOr(Problem, name="Multiples of 3 and 5", expected=233168):
    @Problem.solution()
    def summed_sums(self):
        return self.sum_divisible_by(3, 999) + self.sum_divisible_by(5, 999) - self.sum_divisible_by(15, 999)

    @Problem.solution()
    def brute_force(self):
        return sum(self.multiple_generator(3, 5, max_n=1000))

    @staticmethod
    def multiple_of_any(n, multiples):
        return any(n % i == 0 for i in multiples)

    @classmethod
    def multiple_generator(cls, *args, max_n=None):
        for i in takewhile(lambda n: max_n and n < max_n, count()):
            if cls.multiple_of_any(i, tuple(args)):
                yield i

    @staticmethod
    def sum_divisible_by(n, target):
        p = target // n
        return n * (p * (p + 1)) / 2
