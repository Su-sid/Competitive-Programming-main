class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        temp_ref=dict()
        for count, value in enumerate(nums):
            temp_ref[value]= count
        for current, expected in operations:
            nums[temp_ref[current]] = expected
            temp_ref[expected] = temp_ref[current]
           
        return nums