class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        arrDict = dict()
        count = 0
        for i in nums:
            if i in arrDict and arrDict[i] > 0:
                arrDict[i] -= 1
                count += 1
            else:
                arrDict[k-i] = arrDict.get(k-i, 0) + 1
        return count