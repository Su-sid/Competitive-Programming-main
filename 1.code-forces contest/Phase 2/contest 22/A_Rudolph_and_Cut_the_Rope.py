t= int(input())

for _ in range(t):
    n = int(input())
    total=0
    for _ in range(n):
        a,b = map(int,input().split()) 
        
        if a > b :
            total+=1

    print(total)
       
