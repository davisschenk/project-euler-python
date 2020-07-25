from math import factorial

from problem import Problem


class LatticePaths(Problem, name="Lattice paths", expected=137846528820):
    @Problem.solution()
    def factorials(self, width=20, height=20):
        return factorial(width + height) / (factorial(height) * factorial(width))
