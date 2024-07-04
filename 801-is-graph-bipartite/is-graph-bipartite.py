from collections import defaultdict, deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colored= [-1]*(len(graph))
  
        for startNode in range(len(graph)):
            if colored[startNode]==-1:
                queue= deque([startNode])
          
                colored[startNode]= 0

                while queue:
                    node= queue.popleft()
                    for ind in graph[node]:
                        # neighbours not visited
                        if colored[ind]==-1:
                            colored[ind]= 1- colored[node]
                            queue.append(ind)

                        elif colored[ind]== colored[node]:
                            return False
                        
        return True

        # print(colored)
  
        # return bfs(0, graph)
            

