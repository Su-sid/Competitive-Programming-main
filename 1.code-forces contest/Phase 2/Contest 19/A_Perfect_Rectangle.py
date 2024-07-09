t = int(input())
results = []

def is_perfect_square(x):
    if x < 0:
        return False
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return True
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

for _ in range(t):
    
    n = int(input())
    marbles = list(map(int, input().split()))
    total_marbles = sum(marbles)
    
    if is_perfect_square(total_marbles):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)