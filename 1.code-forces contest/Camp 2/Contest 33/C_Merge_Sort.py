n, k = map (int, input().split())

def mergeSort(left, right):

    global k 

    if k == 1 or left + 1 == right:
        return 
    
    k -= 2

    mid = (left+right )// 2
    arr[mid -1], arr[mid] = arr[mid],arr[mid-1]

    mergeSort(left, mid)
    mergeSort(mid, right)

if k % 2 == 0 or k > 2*n-1:
    print(-1)

else:
    arr= [i for i in range(1, n+1)]

    mergeSort(0, n)

    if k == 1:
        print(*arr)

    else:
        print(-1)
