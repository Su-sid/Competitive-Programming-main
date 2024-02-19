class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if a < b + c:
                return a+b+c
        return 0
        
        