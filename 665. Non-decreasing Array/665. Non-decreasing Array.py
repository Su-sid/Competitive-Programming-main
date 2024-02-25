class Solution:
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        
        modification_needed = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if modification_needed == 1:
                    return False
                modification_needed += 1
               
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]  
                else:
                    nums[i] = nums[i - 1]  
        return True
