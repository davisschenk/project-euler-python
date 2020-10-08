from itertools import chain

from problem import Problem
from utils.math import product
from utils.path import load_file


def load_grid():
    with load_file("p011_grid.txt") as r:
        return [[int(num) for num in line.strip().split(" ")] for line in r]


class LargestGridProduct(Problem, name="Largest product in a grid", expected=70600674):
    grid = load_grid()

    @Problem.solution()
    def basic_search(self):
        """
        Searches through all diagonally, horizontally or vertically adjacent numbers with a length of 4
        """
        all_adjacent = chain(
            self.adjacent_horizontal(self.grid, 4),
            self.adjacent_vertical(self.grid, 4),
            self.adjacent_diagonal(self.grid, 4, direction=1),
            self.adjacent_diagonal(self.grid, 4, direction=-1)
        )

        return max(map(product, all_adjacent))

    @classmethod
    def adjacent_horizontal(cls, arr, length):
        for row in arr:
            for column_index in range(0, len(row) - length):
                yield row[column_index:column_index + length]

    @classmethod
    def adjacent_vertical(cls, arr, length):
        for row_index, row in enumerate(arr):
            for column_index in range(len(row)):
                if row_index + length <= len(arr):
                    yield [arr[row_index + i][column_index] for i in range(length)]

    @classmethod
    def adjacent_diagonal(cls, arr, length, direction=1):
        for row_index, row in enumerate(arr):
            for column_index in range(len(row)):
                if row_index + length <= len(arr) and column_index + length <= len(arr[row_index]):
                    if direction == 1:
                        yield [arr[row_index + i][column_index + i] for i in range(length)]
                    elif direction == -1:
                        yield [arr[row_index + i][column_index - i + length - 1] for i in range(length)]
