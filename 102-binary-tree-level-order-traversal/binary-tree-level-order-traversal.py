# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  
        result= []

        if not root:
            return result

        q= deque([root])

        while q:
            currLevelArr= []
            currLen= len(q)
         
            for _ in range(currLen):
                head= q.popleft()
                currLevelArr.append(head.val)

                if head.left:
                    q.append(head.left)

                if head.right:
                    q.append(head.right)

            result.append(currLevelArr)

        return result


        
