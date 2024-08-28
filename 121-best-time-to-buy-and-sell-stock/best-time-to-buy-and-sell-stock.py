class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0 
        # startVal= prices.index(min(prices))

        # print(startVal)
        # if startVal == len(prices)-1:
        #     return profit

        # maxVal= float('-inf')


        # for i in range(startVal, len(prices)):
        #     maxVal= max (maxVal, prices[i])
            
        #     profit= maxVal- prices[startVal]

        # return profit
            

        profit = 0 
        left, right = 0, 1
        # maxV

        while right < len(prices):

            if prices[left]< prices[right]:
                maxVal= prices[right]-prices[left]
                profit= max(maxVal, profit)
            else:
                left=right
            right+=1
        return profit
