class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
        
        def bfs(start, end):
            q = deque()
            q.append((start,1))
            seen = set()
            
            while q:
                for _ in range(len(q)):
                    node, res = q.popleft()
                    if node == end:
                        return res
                    seen.add(node)
                    
                    for n in graph[node]:
                        if n not in seen:
                            q.append((n,res*graph[node][n]))
            
            return -1.0
        
        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(bfs(a,b))
        
        return res
#         graph = defaultdict(dict)

#         for (u, v), val in zip(equations, values):
#             graph[u][u] = graph[v][v] = 1
#             graph[u][v] = val
#             graph[v][u] =frac 1 / val

#         print(graph)

#         # for k in graph:
#         #     for i in graph[k]:
#         #         for j in graph[k]:
#         #             graph[i][j] = graph[i][k] * graph[k][j]

#         # return [graph[u].get(v, -1) for u, v in queries]
