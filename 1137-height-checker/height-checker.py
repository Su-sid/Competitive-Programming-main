class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights=sorted(heights)
        count=0
        for i, num in enumerate(sorted_heights):
            if not num== heights[i]:
                count+=1
        return count

