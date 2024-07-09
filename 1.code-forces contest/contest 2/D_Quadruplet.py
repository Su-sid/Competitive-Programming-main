n,  target = list(map(int, input().split()))
#8   #15
arr = list(map(int, input().split()))

#int_values = list(map(int, input().split()))
#[3, 2, 5, 8,][ 1, 3, 2, 3]
#list starts from  index 1
#Print four integers: the positions of the values. 

#create all posible two sums 
nums={}
for i in range(n):
    for j in range(i):
        if arr[i]+ arr[j] in nums:
            nums[arr[i]+arr[j]].add(i)
            nums[arr[i]+arr[j]].add(j)
        else:
            nums[arr[i]+arr[j]]= set([i, j])

for i in range(n):
    for j in range(i):
        num=nums[i]+ nums[j]
        nums[num].remove(i)
        nums[num].remove(j)
        ans= set([i,j])
        
        
        if target - num in nums:
            for index in nums[target - num]:
                ans.add(index)
            if len
            
            print(nums[num], nums[target- num])