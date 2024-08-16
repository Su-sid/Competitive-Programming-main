class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(memo, n, start):
            if n == 0:
                return 1
            if n < 0:
                return 0

            if memo[n][start] != -1:
                return memo[n][start]
            
            memo[n][start] = 0
            
            for i in range(start, len(coins)):
                coin = coins[i]
                if n - coin >= 0:
                    memo[n][start] += dp(memo, n - coin, i)
            
            return memo[n][start]

        # def coinChangeII(amount, coins):
        memo = [[-1] * len(coins) for _ in range(amount + 1)]
        return dp(memo, amount, 0)
