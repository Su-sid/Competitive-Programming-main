class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        totalArr=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        # total=

        return sum(totalArr[:k])