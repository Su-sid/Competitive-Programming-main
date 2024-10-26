class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        result= 0 

        heaters.sort()
        for house in houses:
            
            left = 0 
            right = len(heaters) - 1 
            minimum_distance = float('inf')

           
            while left <= right:
                mid = (left + right) // 2
                distance = abs(heaters[mid] - house)
                minimum_distance = min(minimum_distance, distance) 

                
                if heaters[mid] >= house:
                    right = mid - 1
                else:
                    left = mid + 1
            
            result = max(result, minimum_distance) 
        
        return result
