n = int(input())
lst= list()
for i in range(1, n+1):

    lst.append(i)
    a=sorted(lst,reverse=True)
print(' '.join(map(str,a)))