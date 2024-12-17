class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph= defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        visited= set()
        # total = 0 
        def dfs(node, total):
            if node in visited:
                return 0 
            visited.add(node)
            tempTotal= 0
            for neighbor in graph[node]:
                tempTotal+= dfs(neighbor, 2)
            if not hasApple[node] and tempTotal==0:
                return 0 
            return total+ tempTotal
        return dfs(0, 0)






