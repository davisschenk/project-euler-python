from problem import Problem
from utils import path

file = "p018_triangle.txt"


class MaximumSumPath(Problem, name="Maximum path sum I", expected=1074):
    @Problem.solution()
    def sum_all(self):
        print(self)
        """
        This approach goes from the bottom up and add the maximum number to the number above
        """
        triangle = list(self.load_triangle())

        for row in range(len(triangle) - 2, -1, -1):
            for column in range(row + 1):
                triangle[row][column] += max(triangle[row + 1][column], triangle[row + 1][column + 1])

        return triangle[0][0]

    @classmethod
    def load_triangle(cls):
        with path.load_file(file) as r:
            for line in r.readlines():
                numbers = line.split(" ")
                yield list(map(lambda n: int(n.strip()), numbers))
