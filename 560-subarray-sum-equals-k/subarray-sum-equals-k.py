# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         left=result =total= 0

#         length= len(nums)
#         for right in range( length):
#             total += nums[right]
#             # print(total)
#             while total>= k:
#                 if total==k:
#                     result =max(result, right -left +1)
#         #repeat reducing total until it matches K 
#             # while total > k  :#and  left <= right:
#                 # print(nums[left])
#                 total -= nums[left]
#                 left+=1
            
#             # right+=1
#         return result

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        sums = defaultdict(int)
        count = 0

        for a in [0] + list(accumulate(nums)):
            count   += sums[a-k]
            sums[a] += 1
        
        return count