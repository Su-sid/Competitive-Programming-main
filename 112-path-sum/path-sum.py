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

            if not(root.left or root.right):
                
                
                if total== targetSum: 
                    self.final= True
                    # self.final.add(True)
            

            dfs(root.left,total)
            dfs(root.right,total)
            
        print(dfs(root, 0))
        return self.final
        # return final
           

        # return True if dfs(root, 0) else False

        