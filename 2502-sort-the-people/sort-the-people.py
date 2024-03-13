class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #decending is from Top -> Bottom        
        sorted_people= sorted(list(zip(names, heights)), reverse=True, key= lambda heights: heights[1])
        print(sorted_people)
        # unpack to get the name and height after sorting.
        name , height =zip(*sorted_people) 
        return name