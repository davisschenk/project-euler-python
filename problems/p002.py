import math

from problem import Problem


class SumEvenFib(Problem, name="Even Fibonacci numbers", expected=4613732):
    @staticmethod
    def fib(limit=None):
        curr, next_value = 0, 1
        while limit is None or curr < limit:
            yield curr
            curr, next_value = next_value, curr + next_value

    @Problem.solution()
    def naive(self):
        """
        Loop through all fibonacci numbers
            if number is even
                add to sum
        """
        current_sum = 0
        for n in self.fib(limit=4_000_000):
            if n % 2 == 0:
                current_sum += n

        return current_sum

    @staticmethod
    def even_fib(limit=None):
        prime_one, prime_two = 0, 2

        while limit is None or prime_two <= limit:
            yield prime_two

            prime_one, prime_two = prime_two, 4 * prime_two + prime_one

    @Problem.solution()
    def use_only_even(self):
        """
        Sum all even fibonacci numbers
        """
        return sum(self.even_fib(limit=4_000_000))

    @classmethod
    def nth_fib_number(cls, n):
        five_s = math.sqrt(5)
        phi = (1 + five_s) / 2
        return round(pow(phi, n) / five_s)
