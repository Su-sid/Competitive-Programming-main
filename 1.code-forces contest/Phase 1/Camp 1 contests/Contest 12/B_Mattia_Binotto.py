from itertools import accumulate

i = int(input())
count=0
nums= sorted(map(int, input().split()))
prefixsum= list(accumulate(nums,initial=0))

for i, num in enumerate(nums):
    if num>= prefixsum[i]:
        count+=1
        
print(count)
       