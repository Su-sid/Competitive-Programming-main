n, t = list (map(int, input().split()))
arr = list (map(int, input().split()))
# print(n, t, arr)
# arr.sort()
left= 0
i =0
cusum= 0
count=0
while i < len(arr):
    cusum += arr[i]
    while cusum > t:
        cusum-= arr[left]
        left+=1
    count= max(count, i-left+1)
    i+=1
# print(cusum)
print(count)

