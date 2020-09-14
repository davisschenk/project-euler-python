from problem import Problem
from utils.path import load_file


def load_numbers():
    with load_file("p013_numbers.txt") as r:
        return [int(n) for n in r]


class LargeSum(Problem, name="Large Sum", expected=5537376230):
    numbers = load_numbers()

    @Problem.solution()
    def naive(self):
        """
        Sum all numbers and get first 10 chars
        """
        s = sum(self.numbers)

        return str(s)[:10]

    @Problem.solution()
    def first_eleven(self):
        """
        This is technically slower for this example but should use less memory and work for larger numbers
        """
        s = sum(int(number / (10 ** 39)) for number in self.numbers)

        return str(s)[:10]
