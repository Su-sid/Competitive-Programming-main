from collections import defaultdict, deque

nodes,allowedVal = list(map(int, input().split()))
cats = list(map(int, input().split()))
graph= defaultdict(list)

for _ in range(nodes-1):
    fro, to= map(int,input().split())
    graph[fro].append(to)
    graph[to].append(fro)

# print(graph)

def bfs(graph,allowedVal,cats):
    queue= deque()
    queue.append((1,0))
    visited= set()
    ans= 0

    while queue: #is not empty
        #iterate over all the values in the queue
        
        for _ in range(len(queue)):
            #pop the current root element ontop of queue
            node, countOfCats= queue.popleft()
            
            if node in visited:
                continue    
            visited.add(node)

            if cats[node-1]:# 1 is same as True and 0 as False
                countOfCats+=1
            else:
                countOfCats=0

            if countOfCats >allowedVal:
                continue
          
            #move to the neighbouring nodes
            is_leaf = True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    is_leaf = False
                    queue.append((neighbor, countOfCats))
            
            # If it's a leaf and valid path, count it as an answer
            if is_leaf:
                ans += 1
    return ans

print(bfs(graph,allowedVal,cats))
