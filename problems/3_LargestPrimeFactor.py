from math import sqrt
from problem import Problem


class LargestPrimeFactor(Problem, name="Largest prime factor"):
    number = 600851475143

    @Problem.solution()
    def check_all(self, n=number):
        factor = 2
        last = 1

        while n > 1:
            if n % factor == 0:
                last = factor
                n = n // factor

                while n % factor == 0:
                    n = n // factor

            factor += 1
        return last

    @Problem.solution()
    def check_only_odd(self, n=number):
        if n % 2 == 0:
            n = n // 2
            last = 2
            while n % 2 == 0:
                n = n // 2
        else:
            last = 1

        factor = 3

        while n > 1:
            if n % factor == 0:
                n = n // factor
                last = factor

                while n % factor == 0:
                    n = n // factor
            factor += 2

        return last

    @Problem.solution()
    def simple(self, n=number):
        div = 2

        while n != 0:
            if n % div != 0:
                div += 1
            else:
                max_factor = n
                n /= div
                if n == 1:
                    return max_factor

    @Problem.solution()
    def squared(self, n=number):
        if n % 2 == 0:
            last_factor = 2
            n //= 2

            while n % 2 == 0:
                n //= 2
        else:
            last_factor = 1

        factor = 3
        max_factor = sqrt(n)

        while n > 1 and factor <= max_factor:
            if n % factor == 0:
                n //= factor
                last_factor = factor
                while n % factor == 0:
                    n //= factor
                max_factor = sqrt(n)
            factor += 2

        if n == 1:
            return last_factor
        return n




