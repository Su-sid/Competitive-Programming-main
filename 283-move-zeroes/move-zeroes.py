class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        count = 0  # Count of non-zero elements/index position

        #replace push non-zero to the start of list. 
        for i in range(size):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        
        #replace the zero at the end of nums
        for _ in range(count, size):
            nums[count] = 0
            count += 1
        
        return nums