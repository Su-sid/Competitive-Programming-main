"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs (node):
            if node is None:
                return 0
            if node.children is None:
                return 1
            maxD= 0     

            for child in node.children:
                childMax = dfs(child)
                maxD= max(maxD,childMax)
            return maxD +1

        return dfs(root)
                
        