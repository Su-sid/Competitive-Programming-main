n = int(input ())
nums = list(map(int,input().split()))
# define a odd/even function
nums.sort()

finalNums= []

def isEven( num: int)-> bool:
    if num % 2== 0:
        # return even number true
        return True 
    return False

N= n//2
if not isEven(n):
    N= (n//2)+1

for i in range( N):
    finalNums.append(nums[i])
    if i ==(n-1-i):
        continue 
    finalNums.append(nums[n-1-i])    

print(" ".join((map(str, finalNums))))

