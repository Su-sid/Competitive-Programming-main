import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)

        return hq.nlargest(k, nums)[-1]
