
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n= len(nums)
#         res=[1]* n
#         prefix=1
#         postfix=1

#         for i in range(n):
#             res[i]= prefix
#             prefix*= nums[i]
#         for i in range(n-1, -1,-1):

#             res[i]*= postfix
#             postfix*= nums[i]
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        output[0] = 1
        for i in range(1, len(output)):
            output[i] = output[i-1] * nums[i-1]
        prod = 1
        for i in range(len(output)-2, -1, -1):
            prod *= nums[i+1]
            output[i] = output[i] * prod
        return output



    