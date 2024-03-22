class Solution:
    def minPairSum(self, nums: List[int]) -> int:
       

        nums.sort()

        left=maxval=0
        right = len(nums)-1

        while left <right:
            maxval= max(maxval, nums[left]+nums[right])
            left+=1
            right-=1
        return maxval
