# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curMin = float('inf'), curMax = float('-inf')):
            if not node:
                return curMax - curMin

            MIN = min(curMin, node.val)
            MAX = max(curMax, node.val)
            left = dfs(node.left, MIN, MAX)
            right = dfs(node.right, MIN, MAX)

            return max(left, right) 

        return dfs(root)