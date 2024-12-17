
for _ in range( int(input())):
    n,operations= map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0
    while operations> 0:
        while a[cnt] > 0:
            a[n - 1] += 1
            a[cnt] -= 1
            operations-= 1
            if operations<= 0:
                break
        if a[cnt] == 0:
            cnt += 1
        if cnt == n - 1:
            break
    print(*a) 
