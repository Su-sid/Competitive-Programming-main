from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)


for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

check = list(map(int, input().split()))

bfs_order = []
queue = deque([1])
visited = [False] * (n + 1)
visited[1] = True

while queue:
    node = queue.popleft()
    bfs_order.append(node)
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

if bfs_order == check:
    print("Yes")
else:
    print("No")
