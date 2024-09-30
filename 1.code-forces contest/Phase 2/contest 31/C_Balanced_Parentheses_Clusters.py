class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) 
        self.rank = [1] * size   
        self.component = size  # initially, each node is its own component

    def find(self, x):
        # Path compression
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
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

def build_graph(n, s):
    stack = []
 
    size= 2 * n
    uf = UnionFind(size)

    for i in range(2 * n):
        if s[i] == '(':
            stack.append(i)
        else:     
            open_idx = stack.pop()
            # x, y =open_idx + 1, i + 1
            x, y =open_idx , i 
            uf.union(x, y)
   
    return uf.component 

t = int(input())  
for _ in range(t):
    n = int(input())  
    s = input()       
    # edges = build_graph(n, s)
    print(build_graph(n, s))
