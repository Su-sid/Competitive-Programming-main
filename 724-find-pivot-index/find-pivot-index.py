# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n = len(nums)
#         prefix_num = 0
#         prefix = []
#         for number in nums:
#             prefix_num += number
#             prefix.append(prefix_num)

#         prefix.append(0)
#         print(prefix)
        
#         i=1
#         while i < n+1:#Exclusive Prefix Sum
#             print(prefix[i-1], (prefix[n] - prefix[i]))
#             if prefix[i-1] == (prefix[n] - prefix[i]):
#                 return i-1
#             i+=1
        
#         return -1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0, nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        prefix.append(0)
        # print(prefix)
        for i in range(1, n+1):
            print(prefix[i-1], (prefix[n] - prefix[i]))
            if prefix[i-1] == (prefix[n] - prefix[i]):
                return i-1
        
        return -1
