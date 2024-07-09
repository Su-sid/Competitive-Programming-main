n = int(input())

def solve(a,b,c):
    return(a+b>=10) or (a+c>=10) or (c+b>=10)

for _ in range(n):
    a,b,c = map(int,input().split())

   
    if solve(a,b,c):
        final='YES'
    else:
        final="NO"
        
    print(final)
    
