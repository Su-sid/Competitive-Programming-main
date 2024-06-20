class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        final=0
        
        for arr in roads:
            fro, to =arr
            graph[fro].append(to)
            graph[to].append(fro)

        for i in graph:
            for j in graph:
                if i== j: continue
                final=max(final, len(graph[i]) + len(graph[j]) - (i in graph[j]))
        return final
