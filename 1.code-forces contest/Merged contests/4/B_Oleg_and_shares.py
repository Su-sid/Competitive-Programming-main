# n,k= map(int, input().split())

# nums = sorted (map(int, input().split()))

# firstNum = nums[0]

# if firstNum %k ==0:
#     numLen= len(nums)-2
#     Acount=0

#     for i in range(1, len(nums)):
#         while nums[i] != firstNum:
#             nums[i]-=k
#             Acount+=1

#             # print(nums)
#     print(numLen*Acount)
        
# else:
#     print (-1)

n, k = map(int, input().split())
prices = list(map(int, input().split()))

min_price = min(prices)

total_steps = 0

for price in prices:
    diff = price - min_price

    if diff % k != 0:
        total_steps=-1
        break
    
    total_steps += diff // k

print( total_steps)