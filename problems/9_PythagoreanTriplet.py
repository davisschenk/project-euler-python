from problem import Problem
from utils.math import gcd
from math import ceil, sqrt


class PythagoreanTriplet(Problem, name="Special Pythagorean triplet"):
    @Problem.solution()
    def brute_force(self, ts=1000):
        for a in range(3, round((ts-3)/2)):
            for b in range(a+1, round((ts-1-a)/2)):
                c = ts-a-b

                if c*c == a*a + b*b:
                    return a * b * c

    @Problem.solution()
    def parametrisation(self, ts=1000):
        s2 = ts / 2
        mlimit = ceil(sqrt(s2)) - 1

        for m in range(2, mlimit):
            if s2 % m == 0:
                sm = s2 / m
                while sm % 2 == 0:
                    sm /= 2

                if m % 2 == 1:
                    k = m+2
                else:
                    k = m+1

                while k < 2*m and k <= sm:
                    if sm % k == 0 and gcd(k, m) == 1:
                        d = s2/(k*m)
                        n = k-m
                        a = d * (m*m-n*n)
                        b = 2 * d * m * n
                        c = d * (m*m+n*n)
                        return a * b * c
                    k += 2



