class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            value=i+1
            if not value  in  nums:
                return value
        return 0

        