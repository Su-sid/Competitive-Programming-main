class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphStore = defaultdict(list)
        visited =set()
        tempArr=list()
        finalArr=list()
        destination= len(graph)-1

        for node, children in enumerate(graph):
            graphStore[node]=children

        def dfs(node):
            visited.add(node)
            tempArr.append(node)

            if node == destination:
                finalArr.append(tempArr[:])
          
            for neighbor in graphStore[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            visited.remove(node)
            tempArr.pop()

        dfs(0)

        return  finalArr

                

