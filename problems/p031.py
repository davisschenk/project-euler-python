from problem import Problem


class CoinSum(Problem):
    @Problem.solution()
    def solution(self):
        return self.combo_count(200, [1, 2, 5, 10, 20, 50, 100, 200])

    @staticmethod
    def combo_count(total, coins):
        dp = [0 for i in range(total + 1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], total + 1):
                dp[j] += dp[j - coins[i]]

        return dp[total]


