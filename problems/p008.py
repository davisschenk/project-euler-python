from problem import Problem
from utils.math import product
from utils.path import load_file


def load_number():
    with load_file("p008_number.txt") as r:
        return r.read().strip()


class LargestProductInSeries(Problem, name="Largest product in a series", expected=23514624000):
    number = load_number()

    @Problem.solution()
    def brute_force(self):
        best = 0
        for start in range(len(self.number)):
            n = self.number[start:start + 13]
            best = max(best, product(map(int, n)))

        return best
