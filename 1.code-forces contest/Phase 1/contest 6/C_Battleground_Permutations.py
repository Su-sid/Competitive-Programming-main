tests=int(input())
MOD = 10**9 + 7

for _ in range(tests):
    
    n= int(input())
    abilities_cheifu=sorted(list(map(int, input().split())))
    abilities_opponent=sorted(list(map(int, input().split())))

    arrangements = 1
    j = 0  
    for i in range(n):
        while j < n and abilities_opponent[j] < abilities_cheifu[i]:
            j += 1
        victories = j - i
        if victories <= 0:
            arrangements = 0
            break
        else:
            arrangements = (arrangements * victories) % MOD
  
    print( arrangements)

