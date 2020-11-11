from problem import Problem
from utils.math import get_digits


class PowerDigitSum(Problem, name="Power digit sum", expected=1366):
    @Problem.solution()
    def naive(self):
        return sum(get_digits(2 ** 1000))
