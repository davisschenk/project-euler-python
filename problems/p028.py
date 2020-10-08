from problem import Problem


class NumberSpiralDiagonals(Problem):
    @classmethod
    def spiral_sum(cls, n):
        if n == 1:
            return 1

        return 4 * (n ** 2) - 6 * (n - 1) + cls.spiral_sum(n - 2)

    @Problem.solution()
    def maths(self):
        return self.spiral_sum(1001)
