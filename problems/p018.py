from problem import Problem
from utils import path


def load_triangle():
    with path.load_file("p018_triangle.txt") as r:
        for line in r.readlines():
            numbers = line.split(" ")
            yield list(map(lambda n: int(n.strip()), numbers))


class MaximumSumPath(Problem, name="Maximum path sum I", expected=1074):
    triangle = list(load_triangle())

    @Problem.solution()
    def sum_all(self):
        """
        This approach goes from the bottom up and add the maximum number to the number above
        """
        for row in range(len(self.triangle) - 2, -1, -1):
            for column in range(row + 1):
                self.triangle[row][column] += max(self.triangle[row + 1][column], self.triangle[row + 1][column + 1])

        return self.triangle[0][0]
