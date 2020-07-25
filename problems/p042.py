from math import sqrt

from problem import Problem
from utils import path

file = "p042_words.txt"


class CodedTriangleNumbers(Problem):
    @classmethod
    def n_from_triangle_num(cls, n: int):
        return (-1 + sqrt(8 * n + 1)) / 2

    @classmethod
    def is_triangle_number(cls, n: int) -> bool:
        return cls.n_from_triangle_num(n) % 1 == 0

    @classmethod
    def load_words(cls):
        with path.load_file(file) as f:
            return [w.strip('"') for w in f.read().split(",")]

    @classmethod
    def is_triangle_word(cls, word):
        letter_sum = sum(ord(l) - 64 for l in word)

        return cls.is_triangle_number(letter_sum)

    @Problem.solution()
    def solution(self):
        return sum(self.is_triangle_word(w) for w in self.load_words())
