class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for candie in candies:
            if candie + extraCandies >= max(candies):
                result.append(True)               
            else:
                result.append(False)
        return result         