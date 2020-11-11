from problem import Problem
from problems.p002 import SumEvenFib


class FirstThousandDigitFib(Problem, name="1000-digit Fibonacci number", expected=4782):
    @Problem.solution()
    def brute(self):
        for index, n in enumerate(SumEvenFib.fib()):
            if len(str(n)) == 1000:
                return index
