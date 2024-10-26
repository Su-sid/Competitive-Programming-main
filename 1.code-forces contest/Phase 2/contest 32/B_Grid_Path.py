
def minCost( n,m , k):
    totalCost= (n-1)+(m-1)*n
    return totalCost==k

for _ in range(int(input())):
    
    n,m,k = list(map(int, input().split()))

    if minCost(n,m, k):
        print('YES')
    else:
        print('NO')