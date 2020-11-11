from problem import Problem
from problems.p004 import LargestPalindromeProduct


class DoubleBasedPalindromes(Problem, name="Double-base palindromes", expected=872187):
    @Problem.solution()
    def solution(self):
        count = 0

        for n in range(1, 1_000_000, 2):
            if LargestPalindromeProduct.is_palindrome(str(n)) and LargestPalindromeProduct.is_palindrome(bin(n)[2::]):
                count += n

        return count
