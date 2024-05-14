class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = l +(r-l)//2

            if nums[mid]>=target: #mid =3 target = 5 
                r= mid - 1

            if nums[mid]< target:
                l= mid + 1
            else:
                l+1
        return l