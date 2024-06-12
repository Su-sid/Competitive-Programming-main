class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        counts = []
        for node in edges :
            if node[0] in counts :
                return node[0]
            if node[1] in counts :
                return node[1]
            counts.append(node[0])
            counts.append(node[1])

        