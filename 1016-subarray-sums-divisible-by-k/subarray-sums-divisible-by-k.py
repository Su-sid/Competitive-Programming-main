class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        length = len(nums)
        prefix_sum = [0]*(length + 1)

        for i in range(length):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        count = 0
        rem_count = [0]*k

        for cur_sum in prefix_sum:
            reminder = cur_sum % k
            count += rem_count[reminder]
            rem_count[reminder] += 1

        return count