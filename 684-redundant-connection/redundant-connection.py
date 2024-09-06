class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) 
        self.rank = [1] * size   
        # to count number of components.
        # self.component = size

    def find(self, currNode):
        # The iterative approach
        # print(currNode, self.parent)
        x= self.parent[currNode]

        while x != self.parent[x]:
            self.parent[x]= self.parent[self.parent[x]]
            x=self.parent[x]
        return x
      
        # The recursive approach
        # if self.parent[currNode] != currNode:
        #     self.parent[currNode] = self.find(self.parent[currNode])
        # return self.parent[currNode]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        
        if rootX == rootY:
            return False
        # if rootX != rootY:
            # Union by rank: attach the smaller tree under the larger tree
            # self.component -= 1

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX

        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY

        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

    # def connected(self, x,y ):
    #     return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size= len(edges)
        unionFind= UnionFind(size+1)

        for edge in edges:
            r1,r2=edge[0], edge[1]
            if not unionFind.union(r1,r2):
            # if unionFind.connected(r1,r2):
                return edge

        # self.parent= [i for i in range(len(edges)+1)]
        # def findRepresentative(node):
        #     if node != self.parent[node]:
        #         return findRepresentative(self.parent[node])
        #     return node

        # redundant= []

        # for edge in edges:
        #     r1= findRepresentative(edge[0])
        #     r2= findRepresentative(edge[1])

        #     if r1==r2:
        #         redundant= edge

        #     

        # return redundant
        