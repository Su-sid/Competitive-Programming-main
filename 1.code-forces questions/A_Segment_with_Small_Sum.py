
n, s = list(map(int, input().split()))

nums = list(map(int, input().split()))

left=0
Acount=0
cusum= 0 

for  right in range(n):# n:
    cusum+=nums[right]
    # progresive decrement
    while cusum > s:
        # print(left)
        cusum-=nums[left]
        left+=1
    
    Acount= max(Acount, right - left+1)
    # right+=1

print(Acount)


