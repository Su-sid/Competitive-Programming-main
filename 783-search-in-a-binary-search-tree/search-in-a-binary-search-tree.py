# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(root):
            #base condition of the recursive function

            if root is None:
                return None

            #evaluates if the node val and search term are same

            if val == root.val:
                return root

            #evaluates to move to search left side of tree

            if val < root.val:
                return search(root.left)

            #evaluates to move to search right side of tree

            # if val > root.val:
            else:
                return search(root.right)
        
        return search(root)