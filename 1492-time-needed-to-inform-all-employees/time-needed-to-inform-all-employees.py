from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # construct the graph representation

        visited = set()
        graph = defaultdict(list)
 
        for node, value in enumerate (manager):
            if value == -1:
                headID= node 
                continue 
            graph[value].append(node)
        visited.add(headID)
   
        def dfs(node):
            aCount= 0

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    aCount= max(aCount, dfs(neighbor)+informTime[node])
            return aCount


        return dfs(headID)


