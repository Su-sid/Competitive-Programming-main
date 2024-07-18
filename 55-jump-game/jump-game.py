class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums  =sorted (nums)

        index=0
        n=len(nums)

        for i in range(n-1,-1,-1):
            if index <= i +nums[i]:
                index=i 
        return True if index==0 else False 
        # while index < n-1:
        #     # print(index)
            
        #     index+=nums[index]

        #     if index== n-1:
        #         return True
        #     else:
        #         return False
    
        

        # print(nums)