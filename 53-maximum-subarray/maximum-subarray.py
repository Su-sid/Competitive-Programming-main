class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current= final= nums[0]
        for i in range(1, len(nums)):
            #kadanes algorithm
            current= max(nums[i], nums[i]+current)
            if current > final:
                final = current
        return final
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = float('-inf')
#         currentSum = 0
        
#         for num in nums:
#             currentSum += num
            
#             if currentSum > maxSum:
#                 maxSum = currentSum
            
#             if currentSum < 0:
#                 currentSum = 0
        
#         return maxSum