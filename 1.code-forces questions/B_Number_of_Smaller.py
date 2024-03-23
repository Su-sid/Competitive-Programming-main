# Read input
m, n = list(map(int, input().split()))
list_m = list(map(int, input().split()))
list_n = list(map(int, input().split()))

results = []
i, j = 0, 0
counts = 0
while j < n:
    while i < m and list_m[i] < list_n[j]:
        i += 1
        counts += 1  
    results.append(counts)
    j += 1  
print(' '.join(map(str, results)))
