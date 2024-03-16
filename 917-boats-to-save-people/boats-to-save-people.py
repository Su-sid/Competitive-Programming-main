class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        counter=0
        left,right= 0,len(people)-1
        
        while left<=right:
            total= limit-people[right]
            right-=1
            counter+=1
            # if left<=right and 
            if total>=people[left]:
                left+=1

      
        return counter


        