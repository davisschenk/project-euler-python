from problem import Problem

# We can reuse our approach for getting the sum of proper divisors
from problems.p021 import AmicableNumbers


class NonAbundantSums(Problem):
    @Problem.solution()
    def solution(self):
        limit = 28123

        # Avoid recalculating these values over and over
        abundants = [i for i in range(12, limit + 1) if self.is_abundant(i)]

        # Lookup array for finding if it is the sum of two abundants
        is_sum_of_two = [False] * (limit + 1)

        # Loop through all combos and if the sum is greater then the limit then that sum can be set in lookup array
        for i in range(len(abundants)):
            for j in range(i, len(abundants)):
                if abundants[i] + abundants[j] <= limit:
                    is_sum_of_two[abundants[i] + abundants[j]] = True

        # Return the sum of all numbers that arnt the sum of two abundant nums
        return sum(index for index, value in enumerate(is_sum_of_two) if not value)

    @staticmethod
    def is_abundant(number):
        return AmicableNumbers.sum_of_proper_divisors(number) > number
