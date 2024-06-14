class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mySet = set()
        for i,j in edges :
            # print(j)
            mySet.add(j)
        ans = []
        # print(mySet)
        for i in range(n):
            if i not in mySet:
                ans.append(i)
        return ans