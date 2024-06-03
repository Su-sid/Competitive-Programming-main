
from collections import Counter
n= int(input())
for _ in range(n):
    string= input().strip()
    total= Counter(string)
    temp=0
    for i in  total:
        temp= max(total[i], temp)

    # print(temp)
    for x in total:
        if total[x]== temp:
            print(x)
    
