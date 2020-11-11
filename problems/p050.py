from problem import Problem
from utils.primes import sieve_of_eratosthenes, simple_is_prime


class ConsecutivePrimeSum(Problem, name="Consecutive prime sum", expected=997651):
    @Problem.solution()
    def brute_force(self):
        upper_bound = 1_000_000
        primes = list(sieve_of_eratosthenes(4000))
        max_length = 0
        max_prime = 0

        for start in range(len(primes)):
            current_length = 0
            for end in range(start, len(primes)):
                s = sum(primes[start:end])
                current_length += 1

                if s > upper_bound:
                    break
                elif simple_is_prime(s) and current_length > max_length:
                    max_length = current_length
                    max_prime = s

        return max_prime
