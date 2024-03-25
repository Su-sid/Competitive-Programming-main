n,m = list(map(int, input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

newarr = []
i= j = 0
while i < n and j < m:
    if arr1[i] > arr2[j]:
        newarr.append(arr2[j])
        j+=1
    else:
        newarr.append(arr1[i])
        i+=1
    # i+=1
    # j+=1
newarr.extend(arr1[i:]) 
newarr.extend(arr2[j:])
print(*newarr)
        
        