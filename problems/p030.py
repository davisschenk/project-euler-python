from problem import Problem
from utils.math import get_digits


class DigitFifthPowers(Problem):
    @Problem.solution()
    def brute(self):
        total = 0
        for i in range(2, 200_000):
            s = sum(j ** 5 for j in get_digits(i))

            if i == s:
                total += i

        return total
