class Solution:
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pointer1, pointer2 = 0, 1
        for num in nums:
            if not num < 0:
                output[pointer1] = num
                pointer1 += 2
            else:
                output[pointer2] = num
                pointer2 += 2
        return output
        