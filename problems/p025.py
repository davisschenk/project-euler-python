from problem import Problem
from problems.p002 import SumEvenFib


class FirstThousandDigitFib(Problem):
    @Problem.solution()
    def brute(self):
        for index, n in enumerate(SumEvenFib.fib()):
            if len(str(n)) == 1000:
                return index
