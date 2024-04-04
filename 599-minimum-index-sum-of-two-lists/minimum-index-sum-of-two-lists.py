class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
     
        store= defaultdict(list)
        if len(list1)>len(list2):
            list1,list2=  list2, list1
        
        for i, num in enumerate(list1):
            Total=0
            if num in list2:
                Total= i + list2.index(num)
                store[Total].append(num)  
        
        final=min(store.items())
        return final[1]





        