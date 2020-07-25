from itertools import count
from math import sqrt

from problem import Problem


class TriPentHexNumbers(Problem):
    @classmethod
    def triangle_number(cls, n: float):
        return n * (n + 1) / 2

    @classmethod
    def triangle_number_inverse(cls, n: float):
        return (-1 + sqrt(8 * n + 1)) / 2

    @classmethod
    def pentagonal_number(cls, n: float):
        return n * (3 * n - 1) / 2

    @classmethod
    def pentagonal_number_inverse(cls, n: float):
        return (1 + sqrt(24 * n + 1)) / 6

    @classmethod
    def hexagonal_number(cls, n: float):
        return n * (2 * n - 1)

    @classmethod
    def hexagonal_number_inverse(cls, n: float):
        return (1 + sqrt(8 * n + 1)) / 4

    @classmethod
    def is_triangle_number(cls, n: float):
        return cls.triangle_number_inverse(n) % 1 == 0

    @classmethod
    def is_pentagonal_number(cls, n: float):
        return cls.pentagonal_number_inverse(n) % 1 == 0

    @classmethod
    def is_hexagonal_number(cls, n: float):
        return cls.hexagonal_number_inverse(n) % 1 == 0

    @Problem.solution()
    def inverses_solution(self):
        for n in count(286):
            t = self.triangle_number(n)

            if self.is_pentagonal_number(t) and self.is_hexagonal_number(t):
                return t
