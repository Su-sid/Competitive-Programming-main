
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res=[1]* n
        prefix=1
        postfix=1

        for i in range( n):
            res[i]= prefix
           
            prefix*= nums[i]
            # print(res, prefix)
        for i in range(n-1, -1,-1):

            res[i]*= postfix
            postfix*= nums[i]
            # print(':',res, postfix)
        return res
