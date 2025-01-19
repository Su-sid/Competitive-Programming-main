n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
cusum = 0
Acount = n + 1 
 
for right in range(n):
    cusum += nums[right]
    
    while cusum >= s:  
        Acount = min(Acount, right - left + 1)
        cusum -= nums[left]
        left += 1

if Acount == n + 1:
    print(-1) 
else:
    print(Acount)
