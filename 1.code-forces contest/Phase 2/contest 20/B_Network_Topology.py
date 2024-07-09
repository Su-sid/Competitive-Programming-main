from collections import defaultdict

n, m = list(map(int, input().split()))

graph= defaultdict(list)

# for f in range(1, n+1):
    # graph[f]
for i in range(m):
    fro, to = list(map(int, input().split()))
    graph[fro].append(to)
    graph[to].append(fro)

def checker(n,graph):
    degreeCount= defaultdict(int)
    for node in graph:
        degreeCount[len(graph[node])]+=1
    # print(degreeCount)
    if degreeCount[1]==2 and degreeCount[2]==n-2:
        return 'bus topology'
    elif degreeCount[2]==n:
        # print(n)
        return 'ring topology'
    elif degreeCount[1]==n-1 and degreeCount[n-1]==1:
        return 'star topology'
    else :
        return 'unknown topology'
    

print(checker(n,graph))

