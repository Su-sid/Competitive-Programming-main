# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total,counter=0,0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
       
        def dfs(root,total):
            if not root:
                return 0

           
            total += root.val

            path_count = store[total - targetSum]
            # print(store[total - targetSum])
            store[total] += 1
            # print(store)
            path_count += dfs(root.left, total)
            path_count += dfs(root.right, total)
            store[total] -= 1
          
            return path_count
        store = Counter({0: 1})     
        return dfs(root, 0)
