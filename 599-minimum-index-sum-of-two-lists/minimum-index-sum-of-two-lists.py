# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
     
#         store= defaultdict(list)
#         if len(list1)>len(list2):
#             list1,list2=  list2, list1
        
#         for i, num in enumerate(list1):
#             Total=0
#             if num in list2:
#                 Total= i + list2.index(num)
#                 store[Total].append(num)  
        
#         final=min(store.items())
#         return final[1]





class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        
        hashmap = {}
        for i, word in enumerate(list1): 
            hashmap[word] = i

        min_index_sum = float("inf")
        for i, word in enumerate(list2):
            if word in hashmap: # if we have a common word
                curr_sum = hashmap[word] + i
                if curr_sum < min_index_sum:
                    min_index_sum = curr_sum
                    answer = [word]
                elif curr_sum == min_index_sum:
                    answer.append(word)

        return answer


                