
n = int(input())
arr= list(map(int, input().split()))
pairSum= sum(arr)//(n//2)
visited= [False] *n
ans= list()

# fast= 1

for slow in range(0, n-1):
    if visited[slow]:
        continue
    for fast in range(1, n):
        if not visited[fast] and  arr[slow]+ arr[fast]== pairSum and fast != slow:
            ans.append((slow+1, fast+1))
            # print(slow, fast)
            visited[slow]=visited[fast]= True
            break
# print(visited)

for val in ans:

    print(val[0], val[1])





