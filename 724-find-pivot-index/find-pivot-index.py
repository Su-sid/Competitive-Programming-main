class Solution:
    
    def get_prefix(self, nums):
        n = len(nums) + 1
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i-1]
        return prefix

    def pivotIndex(self, nums):
        prefix = self.get_prefix(nums)
        total_sum = prefix[-1]  
        for i in range(len(nums)):
            left_sum = prefix[i]
            right_sum = total_sum - prefix[i] - nums[i]
            if left_sum == right_sum:
                return i  
        return -1  
        
obj = Solution()
final = obj.pivotIndex([1,7,3,6,5,6])
print(final)
