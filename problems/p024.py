from itertools import permutations, islice

from problem import Problem


class LexicographicPermutation(Problem, name="Lexicographic permutations", expected=2783915460):
    @Problem.solution()
    def using_itertools(self):
        return ''.join(next(islice(permutations("0123456789"), 1_000_000 - 1, None)))
