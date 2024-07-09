

n=int(input())
arr= list(map(int, input().split()))

ops= []

for i in range(n):
    min_index= i
    for  j in range (i+1, n):
        if arr[j]< arr[min_index]:
            min_index=j
    if min_index != i:
        ops.append((i, min_index))
        arr[i], arr[min_index]= arr[min_index], arr[i]

print(len(ops))

for i,j in ops:
    print(i,j)
