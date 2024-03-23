class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0  
        left = [0] * len(nums)  
        right = [0] * len(nums)  # This will keep count of consecutive 1's to the right of each index

        for i in range(1, len(nums)):
            if nums[i-1] == 1:
                left[i] = left[i-1] + 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i+1] == 1:
                right[i] = right[i+1] + 1
        for i in range(len(nums)):
            max_len = max(max_len, left[i] + right[i])
        return max_len
        