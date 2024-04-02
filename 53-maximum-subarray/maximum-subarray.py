class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current= final= nums[0]
        for i in range(1, len(nums)):
            #kadanes algorithm
            current= max(nums[i], nums[i]+current)
            if current > final:
                final = current
        return final
        