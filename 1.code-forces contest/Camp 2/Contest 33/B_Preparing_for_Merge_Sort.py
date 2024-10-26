# import bisect

# n = int(input())
# arr = list(map(int, input().split()))
# # prev = 5 #float('-inf') 

# used = [False] * n  
# result = []         

# while not all(used):  
#     subsequence = []  
#     prev = float('-inf')  
    
#     for i in range(n):
#         if not used[i] and arr[i] > prev: 
#             subsequence.append(arr[i]) 
#             prev = arr[i] 
#             used[i] = True  

#     print(*subsequence) 


# import bisect

# n = int(input())
# arr = list(map(int, input().split()))

# used = [False] * n
# result = []   
# while not all(used): 
#     subsequence = [] 
#     positions = []   

#     for i in range(n):
#         if not used[i]:  
#             pos = bisect.bisect_right(subsequence, arr[i])  
           
#             if pos == len(subsequence): 
#                 subsequence.append(arr[i]) 
#                 positions.append(i)        
#     for idx in positions:
#         used[idx] = True  

#     print(*subsequence)

import bisect
from collections import defaultdict
n = int(input())
arr =  list(map(int, input().split()))
last =[]
store = dict()

for i in arr:

    index = bisect.bisect_right(last, -i)
        
    if index== len(last):
        last.append( -i)
        store[len(store)]=[i]
    else :
        store[index].append(i)
        last[index]=-i

    # last[index]
# print(store)
for i in range(len(store)):
    print(*store[i])
