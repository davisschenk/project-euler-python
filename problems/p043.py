from itertools import permutations

from problem import Problem
from utils.strings import unique_chars


class SubStringDivisibility(Problem):
    @classmethod
    def check_ss_divisibility(cls, n):
        primes = [2, 3, 5, 7, 11, 13, 17]
        for i, j in zip(range(1, len(n) + 1), range(4, len(n) + 1)):
            if int(n[i:j]) % primes[i - 1] != 0:
                return False

        return True

    @Problem.solution()
    def naive_solution(self):
        total = 0

        for p in permutations("0123456789"):
            p = ''.join(p)
            if self.check_ss_divisibility(p):
                total += int(p)

        return total

    @Problem.solution()
    def backwards_up(self):
        seventeen_multiples = {str(n * 17) for n in range(100 // 17, 1000 // 17)}  # all 3 digit multiples of 17
        seventeen_multiples = filter(unique_chars, seventeen_multiples)  # filter out those with repeat digits

        primes = [13, 11, 7, 5, 3, 2, 1]
        digits = "1234567890"

        for p in primes:
            new_numbers = []
            for seventeen_multiple in seventeen_multiples:
                for d in digits:
                    # only add each digit if it can be added while maintaining divisibility by the prime
                    if d not in seventeen_multiple and int(d + seventeen_multiple[:2]) % p == 0:
                        new_numbers.append(d + seventeen_multiple)
            seventeen_multiples = new_numbers.copy()

        pandigitals = [int(p) for p in seventeen_multiples if p[0] != 0]

        return sum(pandigitals)
