class Solution:
    def rob(self, nums: List[int]) -> int:
        from typing import List

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # dp[i] will store the maximum amount of money that can be robbed from the first i houses.
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the dp array
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            # print(dp)
        
        return dp[n-1]

        