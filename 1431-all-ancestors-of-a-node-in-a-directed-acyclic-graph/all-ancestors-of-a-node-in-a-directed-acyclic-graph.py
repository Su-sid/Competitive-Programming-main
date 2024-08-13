# class Solution:
#     def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         graph= defaultdict(list)
#         # create an adjucency list of all the edges
#         for to, fro in edges:
#             graph[fro].append(to)
#             # graph2[to].append(fro)
#         print (graph)
#         # print (graph2)
        
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize graph, in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Build the graph and count in-degrees
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Perform topological sort using Kahn's algorithm
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
        
        # Convert sets to sorted lists
        result = [sorted(list(ancestor)) for ancestor in ancestors]
        return result