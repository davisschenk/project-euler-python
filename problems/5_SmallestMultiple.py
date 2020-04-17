from problem import Problem
from utils.math import lcm


class SmallestMultiple(Problem, name="Smallest multiple"):
    @Problem.solution()
    def least_common_multiple(self):
        return lcm(range(1, 20))





