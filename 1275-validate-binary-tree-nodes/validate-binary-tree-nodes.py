class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    
        def find_root():
            is_child = [False] * n
            for child in leftChild + rightChild:
                if child != -1:
                    if is_child[child]:  # Early detection of duplicate child
                        return -1
                    is_child[child] = True

            for i in range(n):
                if not is_child[i]:
                    return i     
            return -1
        
        root = find_root()
        if root == -1: 
            return False
        
        seen = {root}
        stack = [root]
        
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
                    if len(seen) > n:  # Early termination if more nodes are seen
                        return False
                
        return len(seen) == n