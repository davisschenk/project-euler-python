from functools import lru_cache
from math import floor

from problem import Problem
from utils.math import product


class ChampernownesConstant(Problem):
    @classmethod
    def naive_nth_champ(cls, n: int):
        c = ''
        for _ in range(1, n):
            c += str(n)

        return int(c[n - 1])

    # https://math.stackexchange.com/a/626217

    @classmethod
    @lru_cache()
    def g(cls, n: int) -> float:
        return (9 * (n + 1) * 10 ** n - 10 ** (n + 1) + 1) / 9

    @classmethod
    def get_interval(cls, n: int) -> int:
        for i, j in zip(range(10), range(1, 10)):
            if cls.g(i) < n < cls.g(j):
                return j

    @classmethod
    def get_n_champ(cls, n: int) -> int:
        a = cls.get_interval(n)

        number_with_digit = 10 ** a - 1 - floor((cls.g(a) - n) / a)
        digit_count = (cls.g(a) - n) % a

        return number_with_digit // (10 ** digit_count) % 10

    @Problem.solution()
    def solution(self) -> float:
        return product(self.get_n_champ(10 ** n) for n in range(7))
