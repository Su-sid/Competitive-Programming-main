number = int(input())
nums= list(map(int, input().split()))
max_num,maximum,counter= 0,0,nums[0]

for num in nums:
    if counter < num:
        maximum +=1 
    else:
        maximum=1
    counter= num
        
    max_num=max(maximum,max_num)

print(max_num)


