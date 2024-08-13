class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # reverse the graph to get indegrees from outdegrees. 
        n =len(graph)

        indegrees= [0]*n
        adj= [[]for i in range(n)]

        # reversing process

        for i in range (n):
            indegrees[i]=len(graph[i])
            for j in graph[i]:
                adj[j].append(i)

        # print(adj)
        # print(graph)
        q=deque()
        res=[]*n
        for i in range(n):
            if indegrees[i]==0:
                q.append(i)
        while q:
            u=q.popleft()
            res.append(u)
            for i in adj[u]:
                if indegrees[i]!=0:
                    indegrees[i]-=1
                if indegrees[i]==0:
                    q.append(i)
        return sorted(res)