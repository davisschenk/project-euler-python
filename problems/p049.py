from problem import Problem
from utils.primes import sieve_of_eratosthenes


class PrimePermutations(Problem, name="Prime permutations", expected=296962999629):
    @Problem.solution()
    def brute_force(self):
        primes = list(sieve_of_eratosthenes(10000))
        primes.remove(1487)

        for start in primes:

            sequence = [start]

            for i in range(1, 5):
                if (s := start + (3330 * i)) in primes:
                    sequence.append(s)
                else:
                    break

            if len(sequence) == 3 and self.all_permutations(sequence):
                return ''.join(map(str, sequence))

    @classmethod
    def all_permutations(cls, items: list):
        return all(set(str(items[0])) == set(str(n)) for n in items)
