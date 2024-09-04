class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def count_lis(start, prev):
            if start == len(nums):
                return 0, 1
            if (start, prev) in memo:
                return memo[(start, prev)]

            taken_length, taken_count = 0, 0
            if nums[start] > prev:
                taken_length, taken_count = count_lis(start + 1, nums[start])
                taken_length += 1

            not_taken_length, not_taken_count = count_lis(start + 1, prev)

            if taken_length  > not_taken_length:
                memo[(start, prev)] = taken_length, taken_count
            elif taken_length  == not_taken_length:
                memo[(start, prev)] = taken_length, taken_count + not_taken_count
            else:
                memo[(start, prev)] = not_taken_length, not_taken_count

            return memo[(start, prev)]

        return count_lis(0, float('-inf'))[1]