# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This will keep track of the count of nodes visited
        self.count = 0
        # This will store the result once we reach the kth node
        self.result = None
        
        def in_order_traversal(node):
            # If the node is None, return
            if not node or self.result is not None:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)
            
            # Visit the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        # Start the in-order traversal from the root
        in_order_traversal(root)
        
        return self.result

        