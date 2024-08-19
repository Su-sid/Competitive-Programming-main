class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(memo, n):
            # it's already calculated, simply return it
            if memo[n]: 
                return memo[n]
            if n == 0:
                return 0

            memo[n] = float("inf")

            for coin in coins:
                if n - coin >= 0:
                    memo[n] = min(memo[n], 1+dp(memo, n-coin)) #min(memo[n], 1+(returns 0) dp(memo, n-coin))
            return memo[n]
        
        memo =defaultdict(int)
        tmp = dp(memo, amount)
        
        if tmp != float("inf"):
            return tmp            
        else:
            return -1

        # return tmp if tmp != float("inf") else -1
        