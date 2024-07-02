# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #convert the tree to a graph and do bfs with a depth counter.  
        graph = defaultdict(list)
        
        # create a graph from the tree
        def dfs(root,graph):
            if not root:
                return

            if root.val not in graph:
                graph[root.val]
                
            #add the node.val to the graph
            # Check and connect the left child
            if root.left:
                tempLeft= root.left.val

                graph[root.val].append(tempLeft)
                graph[tempLeft].append(root.val)

                dfs(root.left, graph)
            
            # check and connect the right child
            if root.right:
                tempRight=root.right.val

                graph[root.val].append(tempRight)
                graph[tempRight].append(root.val)

                dfs(root.right, graph)
            return graph

        dfs(root,graph)

        # use target as the root node and start traverse a depth equal to k. return the nodes that come at that level.     
        queue = deque()
        visited = list()

        queue.append(target.val)
        depth = 0
        
        while queue:
            for _ in range(len(queue)):
                if depth == k:
                    return list(queue)
                node = queue.popleft()
                visited.append(node)

                for i in graph[node]:
                    if i in visited:
                        continue
                    queue.append((i))

            depth+=1
        return []
  