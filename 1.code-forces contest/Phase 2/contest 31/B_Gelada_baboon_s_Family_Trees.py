
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

def geladaBaboons(size, arr):
    uf=  UnionFind(size)
    for i in range( size):
        x, y = i, arr[i] -1
        uf.union( x, y )

    return uf.component 

n= int(input())
arr= list(map(int, input().split()))

print(geladaBaboons(n, arr))
