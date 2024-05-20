# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        hash_map = defaultdict(list)
        
        def search(node, level):
            if not node:
                return level

            hash_map[level].append(node.val)

            # print(node, level)
            return max( search(node.left, level + 1),  search(node.right, level + 1))



        last_level = search(root,1)

        # print(last_level)

        return hash_map[last_level-1][0]


        #  def search(root):
        #     #base condition of the recursive function

        #     if root is None:
        #         return None

        #     #evaluates if the node val and search term are same
        #     if val == root.val:
        #         return root
        #     #evaluates to move to search left side of tree
        #     if val < root.val:
        #         return search(root.left)

        #     #evaluates to move to search right side of tree

        #     # if val > root.val:
        #     else:
        #         return search(root.right)