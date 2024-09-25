class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
                
        def binarySearch(array):
            # left, right = 0 , len(array)-1
            left, right = max(array), sum(array)

            minAnswer = sum(array)

            while left<= right:
                
                capacity = left+ (right- left)//2

                if possible(capacity):
                    minAnswer= min(minAnswer, capacity) 
                    right= capacity-1
                else:
                    left= capacity +1

            return minAnswer

        # returns true if and only if we can do the task in D days.
        def possible(capacity: int) -> bool:
            cusum=0
            ships =1

            for num in weights:
                # if num > capacity: return False

                if cusum + num > capacity:

                    cusum= num
                    ships+=1
                    # if ships> days:
                    #     return False
                else:
                    cusum+=num
            return ships <= days

        return binarySearch(weights)






