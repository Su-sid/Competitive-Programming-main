class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        final = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    final = max(final, x^y)

        return final 