from itertools import combinations

n = int(input())
nums=list()
final= list()
for _ in range (n):
    num=int(input())
    nums.append(num)
    final.append(-(num))
    
final.extend(nums)
# for i in nums:
#     final.append(i)



# print(final)
comb= list( combinations(final, n))
# print(comb)

def ans(comb):

    for i in comb:
        val=sum(i)
        # print(val)
        if val == 0 or val ==360:
            return 'YES'
    return 'NO'   

print(ans(comb))    
# def search(index, current):
#     if index == n:
#         final.append(current[:])
#         return 
    
    

#     for i in nums:
#         current.append(nums[index])
    
#     search(index+1, current)

    


# search(0,[])

# print(True if final == 0 or 360 else False)

