# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    final= False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, total):
            if not root:
                return 0
            total+=root.val
            if not(root.left or root.right) and total== targetSum: 
                self.final= True
            dfs(root.left,total)
            dfs(root.right,total)
            return self.final
        return (dfs(root, 0))