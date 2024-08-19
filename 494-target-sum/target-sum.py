class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        #possible states of this problem are:
        # target -reducing from 3 to 0 and changes in index 
        # memo[0 * len(nums)+1]

        memo=  {}
        
        def dp ( index, total):
            if index == len(nums):
                if total == target:
                    return 1 
                else: return 0 

            if (index, total ) in memo:
                return memo[(index,total)]

            memo [(index, total)]=  (dp(index +1, total+ nums[index])  +    dp (index+1, total - nums[index]))

            return memo[(index, total )]

        return dp(0,0)



        
        
        
        
        # return dp (target, index)
        