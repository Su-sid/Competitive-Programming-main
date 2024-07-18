class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums  =sorted (nums)

        maximum=0
        # n=len(nums)
        for i, num in enumerate(nums):            
            if maximum < i :  
                return False
            maximum= max(num +  i, maximum)
           
        return  True 


    # return True if index == n-1 else False

        # for i in range(n-1,-1,-1):
        #     if index <= i + nums[i]: #4 <=  4 + 4
        #         index=i 
        # return True if index==0 else False 

    