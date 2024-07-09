# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        

        # - tree ( convert to ) vector
        # - sort the vector
        # - sorted vector -> Inorder Traversal
        # - that\'s all
        vector=list()
        print(root)