from problem import Problem
from utils.math import lcm


class SmallestMultiple(Problem, name="Smallest multiple", expected=232792560):
    @Problem.solution()
    def least_common_multiple(self):
        return lcm(range(1, 20))
