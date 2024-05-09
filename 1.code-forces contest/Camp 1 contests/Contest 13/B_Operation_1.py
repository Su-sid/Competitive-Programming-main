
a, m= list(map(int, input().split()))

def min_operations(a, m):
   
    memo = {}

    def recurse(x):
        if x == 0:
            return 0
        if x < 0:
            return float('inf') 
        
        if x in memo:
            return memo[x]
        
     
        opt1 = recurse(x - 1) + 1
        opt2 = recurse(x - 2) + 1
        memo[x] = min(opt1, opt2)
        return memo[x]

    min_ops = recurse(a)

    for i in range(min_ops, 2 * min_ops + 1):
        if i % m == 0 and i >= min_ops:
            return i

    return -1

print(min_operations(a, m)) 
