
from collections import Counter

def checker(a,b,c):
    val= Counter([a,b,c])
    for i in val:
        if val[i]==1:
            print(i)

t= int(input())
for _ in range(t):
    a,b,c= map(int,input().split())
    checker(a,b,c)

