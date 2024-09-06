class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) 
        self.rank = [1] * size   
        # to count number of components.
        self.component = size
    def find(self, x):
        # The iterative approach
        while x != self.parent[x]:
            self.parent[x]= self.parent[self.parent[x]]
            x=self.parent[x]
        return x
        # The recursive approach
    
        # if self.parent[x] != x:
        #     self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank: attach the smaller tree under the larger tree
            self.component -= 1
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # implement the union find class
        n = len(isConnected)
        unionFind= UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    unionFind.union( i, j)

        return unionFind.component
 
        