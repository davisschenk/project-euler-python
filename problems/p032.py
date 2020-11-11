from problem import Problem


class PandigitalProducts(Problem, name="Pandigital products", expected=45228):
    @Problem.solution()
    def brute(self):
        prods = set()

        for i in range(2, 60):
            start = 1234 if i < 10 else 123

            for j in range(start, 10000 // i):
                if self.is_pandigital(f"{i}{j}{i * j}"):
                    prods.add(i * j)

        return sum(prods)

    @staticmethod
    def is_pandigital(number):
        number = str(number)

        return len(number) == 9 and set(number) == set("123456789")
