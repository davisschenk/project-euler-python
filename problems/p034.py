from math import factorial

from problem import Problem
from utils.math import get_digits


class DigitFactorial(Problem, name="Digit factorials", expected=40730):
    @Problem.solution()
    def solution(self):
        total = 0
        for i in range(3, 50000):
            if i == sum(map(factorial, get_digits(i))):
                total += i

        return total
