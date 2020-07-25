from math import factorial

from problem import Problem
from utils.math import get_digits


class FactorialDigitSum(Problem, name="Factorial Digit Sum", expected=648):
    @Problem.solution()
    def naive(self):
        return sum(get_digits(factorial(100)))
