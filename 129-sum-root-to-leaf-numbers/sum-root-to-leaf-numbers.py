# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    totalF= 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root,total):
            if root is None:
                return 0

            total= total*10+ root.val

            if not (root.left or root.right) :
                self.totalF+= total
            
            dfs(root.left, total)
            dfs(root.right, total)

        dfs(root,0)
        return self.totalF
       
