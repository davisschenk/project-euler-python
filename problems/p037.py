from problem import Problem
from utils.primes import sieve_of_eratosthenes


class TruncatablePrime(Problem):
    @Problem.solution()
    def solution(self):
        primes = {k: False for k in sieve_of_eratosthenes(1_000_000)}

        for prime in primes:
            if self.check_truncatable(prime, 1, lambda p: p in primes):
                if self.check_truncatable(prime, -1, lambda p: p in primes):
                    if prime > 7:
                        primes[prime] = True
        print([k for k, v in primes.items() if v])
        return sum(k for k, v in primes.items() if v)

    @classmethod
    def check_truncatable(cls, n, direction, is_prime):
        for i in cls.truncate(n, direction):
            if not is_prime(int(i)):
                return False
        return True

    @staticmethod
    def truncate(n, direction):
        n = str(n)
        for i in range(len(n)):
            if direction == -1:
                if i == 0:
                    # This is necessary because ls[:0] will just return nothing
                    yield n
                else:
                    yield n[:-1 * i]
            elif direction == 1:
                yield n[i:]
