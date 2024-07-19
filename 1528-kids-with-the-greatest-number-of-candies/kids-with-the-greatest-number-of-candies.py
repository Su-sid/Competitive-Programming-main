class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        final= [False]*len(candies)
        for i, candy in enumerate(candies):
            if candy+ extraCandies>= maxCandies:
                final[i]= True

        
        return final 
