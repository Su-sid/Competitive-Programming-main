class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        otherList= selectedList= []
        store= defaultdict(list)
        

        if len(list1)<len(list2):
            selectedList= list1
            otherList=list2
        else:
            selectedList= list2
            otherList=list1
        
        for i, num in enumerate(selectedList):
            Total=0
            if num in otherList:
                Total= i + otherList.index(num)
                
                store[Total].append(num)
            
        
        final=min(store.items(), key=lambda a: a[0])
        return final[1]





        