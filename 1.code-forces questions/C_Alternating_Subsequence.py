for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    
    ans = 0
    cur = nums[0]

    for  left in range(n):
        if (nums[left] < 0 and cur < 0) or (nums[left] > 0 and cur > 0):
            cur = max(cur,nums[left])
        else:
            ans+=cur
            cur = nums[left]
       
    print(ans+cur)

