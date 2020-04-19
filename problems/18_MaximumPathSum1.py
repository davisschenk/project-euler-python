from problem import Problem
from files.inputs import maximum_path_one


class MaximumSumPath(Problem, name="Maximum path sum I"):
    @Problem.solution()
    def sum_all(self):
        """
        This approach goes from the bottom up and add the maximum number to the number above
        """
        triangle = maximum_path_one

        for row in range(len(triangle) - 2, -1, -1):
            for column in range(row + 1):
                triangle[row][column] += max(triangle[row + 1][column], triangle[row + 1][column + 1])

        return triangle[0][0]
