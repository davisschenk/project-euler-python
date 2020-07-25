from problem import Problem


class LongestCollatzSequence(Problem, name="Longest Collatz Sequence", expected=837799):
    @Problem.solution(ignored=True)
    def naive(self):
        """
        Just test all starting numbers
        """

        best = (0, 0)
        for i in range(1_000_000, 0, -1):
            num = i
            count = 0
            while num != 1:
                count += 1
                if num % 2 == 0:
                    num /= 2
                else:
                    num = 3 * num + 1

            if best[1] < count:
                best = (i, count)

        return best[0]

    @Problem.solution()
    def caching_chains(self):
        """
        Caching calculated values and streamlining the sequence and only calculating down to 500,000
        """
        chains = {1: 1}

        def collatz_sequence(n):
            if n in chains:
                return chains[n]

            if n % 2 == 0:
                chains[n] = 1 + collatz_sequence(n / 2)
            else:
                chains[n] = 2 + collatz_sequence((3 * n + 1) / 2)

            return chains[n]

        longest_chain = 0
        answer = 1
        for number in range(1_000_000, 500_000, -1):
            if collatz_sequence(number) > longest_chain:
                longest_chain = collatz_sequence(number)
                answer = number

        return answer
