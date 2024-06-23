# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # arr=[]

        # create a arr of all nodes
        vector=[]

        def dfs(root):

            if not root:
                return
            val= root.val
            dfs(root.left)
            vector.append(val)
            dfs(root.right)
        dfs(root)
        print(vector)
        
        # - tree ( convert to ) vector
        # - sort the vector
        # - sorted vector -> Inorder Traversal
        # - that\'s all
        # create a arr of all nodes

        def tCreate(l,r):
            node = TreeNode()
            # print(node)
            if l> r:
                return 
            mid = (l+r)//2

            node.val= vector[mid]
            node.left= tCreate(l,mid-1)
            node.right=tCreate(mid+1,r)       

            return node

        return tCreate(0,len(vector)-1)
