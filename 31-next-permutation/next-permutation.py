class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3]
        length = len(nums)
        rightmost= length-2

        while rightmost >= 0 and nums[rightmost]>=  nums[rightmost+1]:
            rightmost -=1
        if rightmost ==-1:
            nums[:]=nums[::-1]
            return 
        leftmost =rightmost+1
        
        while leftmost<length and nums[leftmost]> nums[rightmost]:
            leftmost +=1
        leftmost-=1
        nums[rightmost], nums[leftmost]=nums[leftmost],  nums[rightmost]

        left= rightmost+1
        right= length -1

        while left<right:
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1

        