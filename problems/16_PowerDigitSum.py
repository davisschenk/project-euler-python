from problem import Problem


class PowerDigitSum(Problem, name="Power digit sum"):
    @classmethod
    def get_digits(cls, n):
        while n:
            n, d = divmod(n, 10)
            yield d

    @Problem.solution()
    def naive(self):
        return sum(self.get_digits(2 ** 1000))