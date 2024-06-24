# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
          
        def dfs(node,grandparent,parent):
            if not node:
                return 
            
            if grandparent and grandparent%2==0:
                self.ans+=node.val
            
            dfs(node.left,parent,node.val)
            dfs(node.right,parent,node.val)
            
        
        dfs(root,None,None)
        
        return self.ans

            