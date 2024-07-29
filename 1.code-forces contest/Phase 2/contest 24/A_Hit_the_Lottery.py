

denom = [100,20,10,5,1]
    
count=0 
money=int(input())
i=0
n=len(denom)

# while money < 0:
#     print(money)
while i <n and money:
    if denom[i]<= money:
        count+= money//denom[i]
        # print('denom',denom[i])
        # print('m',money)
        # print(money//denom[i])
        
        # print('c',count)
        money=money%denom[i]
    else:
        i+=1

print(count)
    
