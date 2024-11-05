class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphStore = defaultdict(list)
        tempArr=list()
        finalArr=list()
        destination= len(graph)-1

        for node, children in enumerate(graph):
            graphStore[node]=children

        # print(graphStore)
        def dfs(node):
            # add the current node to the tempArr
            tempArr.append(node)

            # print(tempArr)
            if node == destination:
                # copy values from the tempArr to the finalArr
                finalArr.append(tempArr[:])
            # travel through the neighbors 
            for neighbor in graphStore[node]:
                dfs(neighbor)

            tempArr.pop()
        # start the traversal from the fist node. 
        dfs(0)
        return  finalArr

                

