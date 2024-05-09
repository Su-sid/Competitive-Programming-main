import sys
# take input from the users
n, limit= list(map(int, input().split()))
nums= sorted(list(map(int, input().split())))

# add two dummy values. a minimum and a maximum in each list.
nums =[1]+ nums+ [sys.maxsize]

# compare current and next value. If diff > 0: print 'current' else: print -1
print(nums[limit]) if nums[limit+1]- nums[limit]> 0 else print(-1)
    
