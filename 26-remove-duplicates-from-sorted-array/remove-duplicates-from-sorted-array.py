# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         length= len(nums)
#         temp= float("-inf")
#         i=0
        
        
#         for i in range(length-2):
#         # i, num in enumerate(nums):
#             # print('temp',temp)
#             # print('num',nums[i])
#             # print(nums)
#             if temp <= nums[i]:
#                 nums.append(nums.pop(nums[i]))
#             else: 
#                 continue
#             temp=nums[i]
#             # temp=max(nums[i], temp)
#             # i+=1  
                  
#         return len(set(nums))


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
