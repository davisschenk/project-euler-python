from problem import Problem
from problems.p045 import TriPentHexNumbers as Pent


class PentagonNumbers(Problem, name="Pentagon numbers", expected=5482660):
    @Problem.solution()
    def brute_force(self):
        pents = {}

        for i in range(1, 5000):
            if i not in pents.keys():
                pents[i] = Pent.pentagonal_number(i)

            for j in range(i, 5000):
                if j not in pents:
                    pents[j] = Pent.pentagonal_number(j)

                if Pent.is_pentagonal_number(pents[i] + pents[j]) and Pent.is_pentagonal_number(abs(pents[i] - pents[j])):
                    return abs(pents[i] + pents[j])
