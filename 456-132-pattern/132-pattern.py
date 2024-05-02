class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        c= float(-inf)
        stack=[]

        for i in range(len(nums)-1,-1,-1):

            if nums[i]< c:
                return True
            
            while stack and nums[i]> stack[-1]:
                c= stack.pop()
            stack.append(nums[i])
        return False
        