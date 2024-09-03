class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = Counter(nums)
        for i in number:
            if number[i] == 1:
                return i