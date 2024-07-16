class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # total= numOnes+ numZeros + numNegOnes

        totalArr=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        print(totalArr)
        total=sum(totalArr[:k])

        # print(total)



        return total