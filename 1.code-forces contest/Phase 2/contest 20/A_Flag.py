
n, m = map(int, input().split())

flag=list()
for  _ in range(n):
    flag.append(input().strip()) 

def checkerfunc(flag):
    for row in flag:
        if len(set(row)) != 1:
            return False
  
    for i in range(1, n):
        if flag[i] == flag[i - 1]:
            return False
            
    return True

print('YES') if checkerfunc(flag) else print('NO')

   
