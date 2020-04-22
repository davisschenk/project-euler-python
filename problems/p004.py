from problem import Problem


class LargestPalindromeProduct(Problem, name="Largest palindrome product", expected=906609):
    @Problem.solution()
    def brute_force(self):
        best = 0
        for i in range(999, 100, -1):
            for j in range(999, 100, -1):
                if self.is_palindrome(str(i * j)):
                    best = max(best, i * j)

        return best

    @Problem.solution()
    def improved_brute_force(self):
        best = 0
        for i in range(999, 100, -1):
            for j in range(999, i, -1):
                if self.is_palindrome(str(j*i)):
                    best = max(best, i*j)

        return best

    @Problem.solution()
    def improved_search(self):
        best = 0
        step = -1
        j_max = 999

        for i in range(999, 100, -1):
            if i % 11 == 0:
                j_max = 999
                step = -1
            else:
                j_max = 990
                step = -11

            for j in range(j_max, i, step):
                if i*j <= best:
                    break
                if self.is_palindrome(str(j*i)):
                    best = max(best, j * i)

        return best

    @staticmethod
    def is_palindrome(word):
        if word == word[::-1]:
            return True

        return False
