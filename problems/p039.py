from problem import Problem


class IntegerRightTriangles(Problem):
    @Problem.solution()
    def brute_force(self):
        d = {}
        for p in range(1000):
            d[p] = 0

            for a in range(1, p // 3):
                a, _, c = self.get_abc(a, p)

                if c.is_integer():
                    d[p] += 1

        return max(d.items(), key=lambda i: i[1])

    @staticmethod
    def get_abc(a, p):
        b = (p ** 2 - 2 * p * a) / (2 * p - 2 * a)
        c = (a ** 2 + b ** 2) ** 0.5

        return a, b, c

    @staticmethod
    def is_valid_right_triangle(*sides):
        a, b, c = sorted(sides)

        return a ** 2 + b ** 2 == c ** 2
