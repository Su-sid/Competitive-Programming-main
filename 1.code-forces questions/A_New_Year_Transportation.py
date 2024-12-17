#create a graph
from collections import defaultdict

n, t= list(map(int, input().split()))
nums = list(map(int, input().split()))

finalArr= set([1])
# graph = defaultdict(list)
destination = t

for index, value in enumerate(nums):
    u= index+1
    v= u +value
    # graph[u].append(v)
    finalArr.add(v)

if destination in finalArr:
    print('YES')
else:
    print('NO')

# finalArr = graph.values()

# print(finalArr)
# print(graph)

# print(graph)
# visited = set()
# visited.add(1)

# def dfs(curr_index,destination, graph):
#     if curr_index == destination:
#         return True 

#     for neighbor in graph[curr_index]:
#         # print(neighbor, graph[curr_index])
#         if neighbor not in visited:
#             visited.add(curr_index)
#             if dfs(neighbor, destination, graph):
#                 return True 
            
#     return False

# finalAns = dfs(1,destination, graph)

# print('YES' if finalAns else 'NO')
