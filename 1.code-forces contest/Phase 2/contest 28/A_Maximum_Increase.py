n= int(input())

nums = list(map(int, input().split()))

temp = float("-inf")
freq= 0 
tempfreq= 0
# -inf, 1, 7, 2, 11, 15
for i in nums:
    if i <=temp:
        freq=1
    else:
        freq+=1
    tempfreq= max(tempfreq, freq)
    temp= i 

print(tempfreq)



