from problem import Problem
from problems.p032 import PandigitalProducts


class PandigitalMultiples(Problem, name="Pandigital multiples", expected=932718654):
    @Problem.solution()
    def brute_force(self):
        best = 0
        for i in range(0, 10000):
            digit = ""
            n = 1
            while len(digit) < 9:
                digit += str(n * i)
                n += 1

            if PandigitalProducts.is_pandigital(digit):
                best = max(int(digit), best)

        return best

    @Problem.solution()
    def improved_search(self):
        for x in range(9487, 9230, -1):
            x = 100002 * x
            if PandigitalProducts.is_pandigital(x):
                return x

    @staticmethod
    def is_pandigital(n):
        # Bit vector check, this is actually slower then checking with a set
        if not n % 9 == 0:
            return False

        flag = 0

        while n > 0:
            q = 0x1999999a * n >> 32
            flag |= 1 << (n - q * 10)
            n = q

        return flag == 0x3fe
