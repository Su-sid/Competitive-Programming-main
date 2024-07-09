

from collections import defaultdict,deque

n = int(input())

graph = defaultdict(list)

for _ in range(n-1):
    j,k = list(map(int,input().split()))
   
    graph[j].append(k)
    graph[k].append(j)

print(graph)

