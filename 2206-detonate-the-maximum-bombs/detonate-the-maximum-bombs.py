class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        def isRange(i, j):
            xi, yi, ri = bombs[i]
            xj, yj, rj = bombs[j]
            return ri ** 2 >= (xi -xj) ** 2 + (yi -yj) ** 2
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and isRange(i, j):
                    graph[i].append(j)
        
        def dfs(curr, visited):
            visited.add(curr)
            for neib in graph[curr]:
                if neib not in visited:
                    dfs(neib, visited)
                    
            return len(visited)
        
        answer = 0
        for i in range(len(bombs)):
            answer = max(answer, dfs(i, set()))
            
        return answer