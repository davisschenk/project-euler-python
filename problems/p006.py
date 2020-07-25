from problem import Problem


class SumSquareDifference(Problem, name="Sum square difference", expected=25164150):
    @Problem.solution()
    def brute_force(self, limit=100):
        nums = range(1, limit + 1)
        return self.square_of_sum(nums) - self.sum_of_squares(nums)

    @Problem.solution()
    def math(self, limit=100):
        s = limit * (limit + 1) / 2
        s_sq = (2 * limit + 1) * (limit + 1) * limit / 6

        return s ** 2 - s_sq

    @staticmethod
    def square_of_sum(nums):
        return sum(nums) ** 2

    @staticmethod
    def sum_of_squares(nums):
        return sum(num ** 2 for num in nums)
