from problem import Problem
from utils.math import get_digits
from itertools import permutations


class PandigitalProducts(Problem):
    @Problem.solution()
    def brute(self):
        prods = set()

        for i in range(2, 60):
            start = 1234 if i < 10 else 123

            for j in range(start, 10000//i):
                if self.is_pandigital(f"{i}{j}{i*j}"):
                    prods.add(i*j)

        return sum(prods)
    
    @staticmethod
    def is_pandigital(number):
        num_s = str(number)

        return len(num_s) == 9 and set(num_s) == set("123456789")